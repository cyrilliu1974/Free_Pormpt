import numpy as np
import hybrid_search as hs

index = hs.load_index()
emb = hs.ensure_embeddings(index, verbose=False)
from fastembed import TextEmbedding
model = TextEmbedding(model_name=hs.EMB_MODEL)

ART_SLUGS = ("create-photorealistic-campaign-images", "create-product-advertisement-concepts")
art_idx = {}
for gi, e in enumerate(index):
    if any(s in (e.get("path") or "") for s in ART_SLUGS):
        art_idx[gi] = e

def qsim(q):
    qv = np.asarray(next(model.embed([q])), dtype=np.float32)
    n = np.linalg.norm(qv)
    if n > 0:
        qv = qv / n
    sims = emb @ qv
    idx = np.argsort(-sims)
    print(f"\n=== query: {q!r} ===")
    for i in idx[:12]:
        e = index[i]
        print(f"  {sims[i]:.3f}  {e['category']} / {e.get('subcategory')} / {e['title']}")
    print("  -- art files sim --")
    for gi, e in art_idx.items():
        print(f"  {sims[gi]:.3f}  {e['path']}")

for q in ["房地產", "幫我寫一首詩", "real estate", "寫一首詩", "廣告圖"]:
    qsim(q)
