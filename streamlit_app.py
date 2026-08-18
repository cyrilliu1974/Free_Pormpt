# streamlit_app.py — God of Prompt 離線庫 · 雙語 Web 檢索介面 (lexical / hybrid)
# 啟動 / Start:
#   streamlit run streamlit_app.py --server.port 8501 --server.headless true
#
# 功能 / Features:
#  - 中英雙語介面 (Bilingual UI)
#  - 上層分類 → 下層分類 連動下拉 (cascading dropdown)
#  - 選定類別 → 搜尋範圍限定該類別; 未選 → 全域搜尋
#  - 檢索模式切換: 詞彙 Lexical (欄位加權 + 同義/中英擴展) | 混合 Hybrid (推薦, lexical + 本地 embedding + RRF)
#  - 純本地, 不呼叫任何 LLM API
#  - 回傳 路徑 / 選取理由 / 分數 / 完整 prompt / 框架型態 / 相關技能

import os
import sys
import streamlit as st

# 讓 import hybrid_search 可用 (與本檔同目錄)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hybrid_search as hs

PROMPTS_DIR = hs.PROMPTS_DIR

@st.cache_data
def load_index():
    return hs.load_index()

@st.cache_resource(show_spinner=False)
def get_resources():
    # 載入索引 + (必要時) corpus embedding 快取; 首次會下載模型並建立, 之後只讀 .npy
    # 注意: 必須在 Streamlit session 內 (脚本主體) 呼叫, 不可在 import 時期執行,
    # 否則 @cache_resource 的 spinner 會因無 session 而 NoSessionContext,
    # 且 fastembed 多進程會觸發 forkserver 重新 import 本檔造成遞迴崩潰。
    index = load_index()
    emb = hs.ensure_embeddings(index, verbose=False)
    return index, emb

# —— 頁面 ——
st.set_page_config(page_title="Prompt 檢索 / Prompt Search", layout="wide")
st.title("📚 AI Prompt 離線庫 · 檢索介面")
st.caption("AI Prompt Library — Offline Search UI ｜ 中英雙語 / Bilingual")

with st.expander("ℹ️ 使用說明 / How to use", expanded=True):
    st.markdown(
        """
        **中文 / Chinese**
        1. 選擇「大類」(如 Marketing、Real Estate);選了之後下方才會出現對應的「類別」。
        2. 類別可選可不選:選了就把搜尋範圍限制在該類別;都不選則為**全域搜尋**。
        3. 選擇**檢索模式**:`混合 Hybrid`(推薦) / `詞彙 Lexical`(純關鍵字) / `全部顯示 Browse`(瀏覽所選類別下全部 prompt, 須先選 ①大類+②類別)。
        4. 在輸入框打入你的需求(支援中文,會自動展開為英文關鍵字),按「搜尋」。
        5. 結果可展開看完整 prompt、框架型態與相關技能。

        **English**
        1. Pick a **top category** (e.g. Marketing, Real Estate); the **subcategory** dropdown appears below it.
        2. Subcategory is optional: picking one scopes search to that subcategory; leaving both = **global search**.
        3. Choose **retrieval mode**: `混合 Hybrid` (recommended) / `詞彙 Lexical` (pure keyword) / `全部顯示 Browse` (list all prompts in a chosen subcategory — pick ① category + ② subcategory first).
        4. Type your need in the box (Chinese is supported — it auto-expands to English keywords) and press **Search**.
        5. Expand any result to see the full prompt, its framework type and related skills.

        ⚙️ 檢索技術 / Retrieval: 本地 **詞彙語意檢索 (lexical + 同義詞/中英擴展 + 欄位加權)**,可疊加 **本地多語言 embedding + RRF 混合檢索** — **不呼叫任何 LLM API / no LLM API calls**.
        """
    )

# —— 載入索引 + embedding 快取 (首次會下載模型並建立, 之後只讀 .npy) ——
# 必須放在 session 內 (頁面主體), 不可在 import 時期執行, 否則會
# NoSessionContext / fastembed 多進程遞迴崩潰。cache_resource 會讓重跑只讀快取。
with st.spinner("首次載入會下載多語言模型並建立向量快取，請稍候… / "
               "Loading multilingual model & building cache (first run only)…"):
    index, emb = get_resources()

cats = sorted({e["category"] for e in index if e.get("category")})
subs_map = {}
for e in index:
    if e.get("category") and e.get("subcategory"):
        subs_map.setdefault(e["category"], set()).add(e["subcategory"])
subs_map = {k: sorted(v) for k, v in subs_map.items()}

ALL = "(全部 / All)"
cat_opts = [ALL] + cats
def on_cat_change():
    st.session_state.sub = ALL
cat = st.selectbox("① 選擇大類 / Select top category", cat_opts, key="cat", on_change=on_cat_change)
if cat == ALL:
    sub_opts = [ALL]; cat_arg = None
else:
    sub_opts = [ALL] + subs_map.get(cat, []); cat_arg = cat
sub = st.selectbox("② 選擇類別 / Select subcategory", sub_opts, key="sub")
sub_arg = None if sub == ALL else sub

mode = st.radio(
    "③ 檢索模式 / Retrieval mode",
    ["混合 Hybrid (推薦)", "詞彙 Lexical", "全部顯示 Browse"],
    horizontal=True,
    help="Hybrid = 詞彙 + 本地語意 embedding (RRF 融合, dense 只補充詞彙沒抓到的相關項); "
         "Lexical = 純關鍵字/同義/欄位加權; 全部顯示 = 瀏覽所選類別下的全部 prompt (須先選 ①大類 + ②類別)",
)
mode_arg = "hybrid" if mode.startswith("混合") else ("all" if mode.startswith("全部") else "lexical")

with st.form("search_form"):
    q = st.text_input(
        "④ 輸入需求 / Enter your need",
        placeholder="例如 / e.g. 我想評估房地產現金買家報價是否可靠 ｜ write a high-converting landing page ad copy",
    )
    col1, col2 = st.columns([1, 3])
    with col1:
        topN = st.slider("結果數 / Top N", 1, 20, 5)
    with col2:
        st.write("")  # spacer
    submitted = st.form_submit_button("🔍 搜尋 / Search")

if submitted:
    try:
        if mode_arg == "all":
            # 全部顯示: 瀏覽所選類別下的全部 prompt (須先選 ①大類 + ②類別/下一階)
            if not (cat_arg and sub_arg):
                st.info("請先選擇「① 大類」與「② 類別（下一階）」，才能瀏覽該類別底下的全部 prompt。\n"
                        "Pick ① top category and ② subcategory first to list all prompts in that subcategory.")
            else:
                res = hs.search("", topN, cat_arg, sub_arg, "all", index=index, emb=emb)
                st.success(f"該類別共 {res['count']} 筆 prompt / {res['count']} prompts ｜ "
                           f"大類 / category: {cat_arg} ｜ 類別 / subcategory: {sub_arg}")
                if res["count"] == 0:
                    st.info("此類別暫無 prompt。/ No prompts in this subcategory yet.")
                for r in res["results"]:
                    head = f"#{r['rank']} · {r['title']}"
                    with st.expander(head):
                        st.markdown(f"**路徑 / Path:** `{r['path']}`")
                        if r.get("archetype"):
                            st.markdown(f"**框架型態 / Framework:** {r['archetype']}")
                        if r.get("related_skills"):
                            st.markdown("**相關技能 (skills.json) / Related skills:** "
                                        + "; ".join(f"{x['cat']} · {x['skill']}" for x in r["related_skills"]))
                        st.markdown("**完整 Prompt / Full prompt:**")
                        st.code(r["content"], language="markdown")
        else:
            if q.strip():
                res = hs.search(q.strip(), topN, cat_arg, sub_arg, mode_arg, index=index, emb=emb)
                st.success(f"找到 {res['count']} 筆相符 / Found {res['count']} matches"
                           + (f" ｜ 範圍 / scope: {cat_arg or '全部'}{('/ '+sub_arg) if sub_arg else ''}")
                           + f" ｜ 模式 / mode: {mode_arg}")
                if res["count"] == 0:
                    st.info("試試更通用的關鍵字,或瀏覽 prompts/index.md 的分類總覽。\n"
                            "Try broader keywords, or browse the category index in prompts/index.md.")
                for r in res["results"]:
                    head = f"#{r['rank']} · {r['score']} 分 / pts · {r['title']}"
                    with st.expander(head):
                        st.markdown(f"**大類/類別 / Category:** {r['category']} / {r['subcategory']}")
                        if r.get("archetype"):
                            st.markdown(f"**框架型態 / Framework:** {r['archetype']}")
                        st.markdown(f"**路徑 / Path:** `{r['path']}`")
                        if r.get("related_skills"):
                            st.markdown("**相關技能 (skills.json) / Related skills:** "
                                        + "; ".join(f"{x['cat']} · {x['skill']}" for x in r["related_skills"]))
                        st.markdown("**選取理由 / Reasons:** " + "; ".join(r["reasons"]))
                        st.markdown("**完整 Prompt / Full prompt:**")
                        st.code(r["content"], language="markdown")
            else:
                st.warning("請先輸入需求 / Please enter a query first.")
    except Exception as ex:
        st.error("執行檢索時發生錯誤 / Error running search: " + str(ex))
