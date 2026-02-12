# E-Commerce Sales Funnel & Product Insights — Key Insights & Recommendations

## 1. Funnel & Conversion

### What to look at
- **Funnel conversion rates** (`outputs/funnel_conversion_rates.csv`): Count and % at each stage (Visit → Signup → Add to Cart → Purchase).
- **Funnel by segment** (`outputs/funnel_by_device.csv`, `funnel_by_region.csv`, `funnel_by_campaign_source.csv`): Same metrics by device, region, and campaign.

### Typical insights
- **Highest drop-off stage**: Often between Add to Cart and Purchase (cart abandonment) or between Visit and Signup (low signup intent).
- **Device**: Mobile often has lower conversion than desktop; tablet may sit in between.
- **Campaign**: Paid campaigns may show different conversion than organic; email often converts better.

### Recommendations
- **UX**: If drop-off is at **Add to Cart → Purchase**: simplify checkout (fewer steps, guest checkout, clear shipping costs), add trust badges and security messaging, and reduce friction (e.g. one-click pay).
- **Marketing**: If drop-off is at **Visit → Signup**: reduce signup friction (e.g. social login), use lead magnets or incentives, and retarget visitors with signup-focused campaigns.
- **Targeting**: Use funnel_by_region and funnel_by_campaign_source to double down on high-converting segments and run experiments (e.g. landing pages, messaging) on low-converting ones.

---

## 2. Product & Category Performance

### What to look at
- **Top products** (`outputs/top_products.csv`): Revenue and units sold per product.
- **Revenue by category** (`outputs/revenue_by_category.csv`): Revenue, units, and order count per category.

### Typical insights
- A small set of products/categories usually drives most revenue (Pareto).
- Some categories have high revenue but low order count (high AOV); others are high volume, lower AOV.

### Recommendations
- **Promotion**: Feature top-selling products on homepage and in paid campaigns; use them in bundles or “frequently bought together.”
- **Discounts**: Put strategic discounts on mid-tier products to move them into top tier; use clearance for long-tail underperformers.
- **Inventory & assortment**: Stock and prioritize top categories; consider pruning or repositioning weak categories.

---

## 3. Revenue Trends & Seasonality

### What to look at
- **Daily revenue** (`outputs/daily_revenue.csv`): Time series of revenue and orders.
- **Revenue heatmap** (`outputs/revenue_heatmap.png`): Revenue by weekday and hour.

### Typical insights
- Weekends and certain hours (e.g. evening) often show higher revenue.
- Seasonal peaks (e.g. holidays, back-to-school) appear in the daily trend.

### Recommendations
- **Marketing**: Increase ad spend and email sends during peak days/hours and ahead of seasonal peaks.
- **Operations**: Align staffing and inventory with predicted demand from trends.
- **Regional campaigns**: If you have region-level data, schedule campaigns by local peak times.

---

## 4. KPIs (AOV, Revenue, Repeat)

### What to look at
- **KPIs** (`outputs/kpis.csv`): Total revenue, AOV, total orders, repeat purchaser %.

### Recommendations
- **AOV**: Use free shipping thresholds, product recommendations, and bundles to lift AOV.
- **Repeat rate**: Use email/post-purchase flows, loyalty program, and personalized recommendations to increase repeat purchases.

---

## 5. Next Steps (Optional Extensions)

- **Predictive analytics**: Forecast daily/weekly sales by product or region (e.g. ARIMA, Prophet, or simple ML).
- **A/B testing**: Analyze campaign or landing-page tests to attribute impact on funnel stages and conversion.
- **ETL automation**: Schedule data refresh (e.g. nightly) and re-run cleaning, funnel, and EDA so dashboards stay up to date.
