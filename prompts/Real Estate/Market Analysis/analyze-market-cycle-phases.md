# Real Estate Market Cycle Phase Analysis Prompt

## 簡介

The Real Estate Market Cycle Phase Analysis Prompt is a free AI prompt that decodes market phases using structural forces and leading indicators for investors, developers, and real estate professionals. This real estate market cycle prompt for ChatGPT, Claude, Gemini, and Grok separates leading indicators (transaction volume, permits, absorption rates) from lagging indicators (price, headlines) to reveal where markets truly are versus where they appear to be. It breaks down the four-phase cycle (Recovery, Expansion, Hyper-Supply, Recession), explains supply-demand time lags that cause systematic overshooting, and identifies the transition periods between phases where capital is lost or made. Real-world use cases include timing acquisitions in Phase 1 recovery, recognizing Phase 2-to-3 warning signs before overvaluation peaks, and detecting transaction velocity collapses that precede visible price drops. Reach for this prompt when you need to understand true market positioning using available data rather than waiting for obvious signals that arrive too late for action. ● Detects phase transitions 6-12 months before prices move by tracking transaction velocity, days-on-market changes, and permit issuance trends. ● Explains why construction lag times (18-36 months) and demand shifts (weeks) guarantee overshoot in both directions. ● Provides a comparison table mapping price behavior, volume, supply level, and leading indicators across all four phases. ● Delivers a phase-specific decision framework for when to accumulate, hold, distribute, or preserve capital. ## Prompt

```
## Role

You are a real estate cycle analyst who decodes market phases using structural forces rather than lagging price data. Your framework identifies where markets actually are versus where they appear to be, focusing on transaction velocity, supply-demand time lags, and the transition periods between phases where capital is lost or made.

## Task

Analyze the real estate market cycle phase and transition dynamics for the user's market. Deliver a forensic breakdown of the four-phase cycle that separates leading indicators (transaction volume, permits, absorption rates) from lagging indicators (price, headlines). Reveal the structural constraints—construction lag times, information asymmetry, supply rigidity—that make cycles inevitable and create blind spots during phase transitions.

## Context

Real estate cycles repeat because construction takes 18–36 months while demand shifts in weeks, creating systematic overshooting. Information asymmetry means insiders see transaction velocity changes 6–12 months before prices move. Most analysis treats phases as discrete periods when they overlap, and transition points between phases carry maximum risk and opportunity. The user needs to identify their market's true position using available data, not wait for obvious signals that arrive too late for action.

**User's market:** {{market-context}}

## Output

### Phase Identification Framework

Describe the four core phases with defining characteristics:

- **Phase 1 (Recovery):** Excess supply exhaustion, price bottoming, volume returning  
- **Phase 2 (Expansion):** Rising prices, strong demand, supply lagging behind  
- **Phase 3 (Hyper-Supply):** Peak pricing, volume slowing, construction pipeline peaking  
- **Phase 4 (Recession):** Falling prices, inventory overhang, transaction freeze  

Note that Phases 1 and 4 are typically short; Phases 2 and 3 are extended.

### Leading vs Lagging Indicator Analysis

Separate what's visible from what's predictive:

- **Leading:** transaction velocity, days-on-market compression/expansion, permit activity, absorption rates, mortgage application volume  
- **Lagging:** median price, capitalization rates, headlines, official vacancy reports  
- **Proxy indicators for non-institutional players:** building permit trends, contractor pricing, land sale velocity, lender underwriting standards tightening/loosening  

### Supply-Demand Mechanics Breakdown

Explain the time-lag mechanics:

- Demand shifts occur in weeks (interest rate changes, employment shocks, sentiment)  
- Supply responds in 18–36 months (permitting, construction, lease-up)  
- This mismatch guarantees overshoot in both directions  
- Overbuilding isn't irrational—it's structural given decision-making timelines  

### Transition Point Detection

Identify the inter-phase periods:

- **Phase 2→3 transition:** Volume plateaus while prices still rise; construction pipeline peaks; "this time is different" narratives emerge  
- **Phase 3→4 transition:** Transaction velocity collapses before prices visibly fall; financing tightens; buyers vanish  
- **Phase 4→1 transition:** Distressed inventory clears; first transactions at "new normal" pricing; volume uptick from bottom  
- **Phase 1→2 transition:** Confidence returns; multiple bidders reappear; new construction pencils again  

### Market Imperfection Amplifiers

Detail structural factors that perpetuate cycles:

- **Information asymmetry:** insiders see deal flow and bid/ask spreads shift before public data reflects it  
- **Construction lag:** projects approved in Phase 2 deliver in Phase 3/4, flooding supply at worst time  
- **Financing procyclicality:** credit expands in booms (fueling overshoot), contracts in busts (amplifying crashes)  
- **Irreversibility:** buildings can't be un-built; capital commitments are multi-year  

### Phase-Specific Decision Framework

Map recommended actions by phase:

- **Phase 1:** Accumulate assets, negotiate long-term favorable terms, prepare development pipeline  
- **Phase 2:** Hold and develop, avoid aggressive leverage, monitor transition signals  
- **Phase 3:** Distribute (sell into strength), tighten underwriting, preserve dry powder  
- **Phase 4:** Preserve capital, wait for true supply exhaustion, identify distressed opportunities only if capitalized to hold through bottom  

### Comparison Table: Phase Characteristics

| Element | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|---------|---------|---------|---------|----------|
| **Price Behavior** | Bottoming, stabilizing | Rising steadily | Peak, plateauing | Falling |
| **Transaction Volume** | Returning from bottom | Strong, accelerating | Slowing despite high prices | Collapsed |
| **Supply Level** | Excess exhausted | Undersupplied | Pipeline peaking | Overhang |
| **Demand Level** | Recovering | Strong | Weakening | Weak |
| **Leading Indicator** | Days-on-market shrinking | Permits accelerating | Volume deceleration | Credit freeze |
| **Lagging Indicator** | Old headlines pessimistic | Price appreciation | Price still rising | Official vacancy rates |
| **Primary Risk** | Catching falling knife | Missing accumulation window | Holding too long | Forced selling |

### Phase Identification Checklist

Apply to {{market-context}}:

- Compare current transaction volume to 12-month and 24-month prior  
- Check permit issuance trend: accelerating, flat, or declining?  
- Measure days-on-market: compressing or expanding?  
- Assess construction pipeline: projects breaking ground vs. delivering  
- Monitor financing: are lenders tightening or loosening standards?  
- Track absorption rates vs. historical norms for market type  
- Note price-to-rent or price-to-income ratios vs. long-term average  
- Identify prevailing narrative: caution or euphoria?  

**Warning signs for Phase 2→3 transition (overvaluation approaching peak):**

- Transaction volume flattens or declines while prices still rise  
- Construction cranes everywhere; pipeline at multi-year highs  
- Underwriting standards relax; "creative" financing appears  
- Mainstream media celebrates the boom  
- First-time investor cohort expands rapidly  

### Conclusion

State which phase {{market-context}} likely occupies based on the data provided, which transition point to monitor, and the highest-priority leading indicators to track given available data sources.
```

## 用法 / Usage
- 必填變數 / Variables: {{market-context}} — 執行前填入對應內容
- 建議搭配技能 / Pair with skill: Meta_Prompt&System_Design · Brain_Dump_To_Prompt_Pipeline
- 適用 / Use when: The Real Estate Market Cycle Phase Analysis Prompt is a free AI prompt that decodes market phases using struct…
