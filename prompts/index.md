# AI Prompt Library — 分類總索引

> 分類結構: **大類 (category) → 類別 (subcategory)**,共 21 大類 / 143 類別 / 6398 個 prompt

## 大類一覽

| 大類 | 類別數 | prompt 數 | 進入 |
|---|---:|---:|---|
| AI Agents | 1 | 2 | [AI Agents](./AI%20Agents/index.md) |
| Art and Design | 16 | 808 | [Art and Design](./Art%20and%20Design/index.md) |
| Audio | 2 | 16 | [Audio](./Audio/index.md) |
| Careers | 4 | 94 | [Careers](./Careers/index.md) |
| Coding | 16 | 497 | [Coding](./Coding/index.md) |
| Customer Service | 6 | 167 | [Customer Service](./Customer%20Service/index.md) |
| Data Analysis | 7 | 194 | [Data Analysis](./Data%20Analysis/index.md) |
| Education | 8 | 436 | [Education](./Education/index.md) |
| Finance | 8 | 295 | [Finance](./Finance/index.md) |
| Human Resources | 8 | 334 | [Human Resources](./Human%20Resources/index.md) |
| Legal | 6 | 216 | [Legal](./Legal/index.md) |
| Marketing | 9 | 701 | [Marketing](./Marketing/index.md) |
| Operations | 5 | 376 | [Operations](./Operations/index.md) |
| Productivity | 6 | 379 | [Productivity](./Productivity/index.md) |
| Real Estate | 7 | 145 | [Real Estate](./Real%20Estate/index.md) |
| Research | 6 | 279 | [Research](./Research/index.md) |
| SEO | 6 | 512 | [SEO](./SEO/index.md) |
| Sales | 7 | 142 | [Sales](./Sales/index.md) |
| Strategy | 8 | 444 | [Strategy](./Strategy/index.md) |
| Video | 1 | 2 | [Video](./Video/index.md) |
| Writing | 6 | 359 | [Writing](./Writing/index.md) |

## 如何查詢 prompt

- **命令列查詢**:
  ```
  node query.mjs "我想寫落地頁廣告文案"
  ```
- 腳本會對標題 / 關鍵字 / 大類 / 類別 / 適用對象 / 內文做評分,回傳最相關的 prompt 路徑、內容與選取理由。
- 搜尋索引: `prompts/_search-index.json` (由本腳本自動產生)。
