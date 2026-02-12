-- E-Commerce Funnel & KPI Queries
-- Run against your data warehouse (BigQuery, Snowflake, Redshift, etc.)
-- Adapt table/column names to your schema.

-- ============================================
-- 1. Funnel stages (one row per session)
-- ============================================
CREATE OR REPLACE VIEW funnel_sessions AS
SELECT
    session_id,
    user_id,
    MAX(CASE WHEN event_type = 'visit'       THEN 1 ELSE 0 END) AS visit,
    MAX(CASE WHEN event_type = 'signup'      THEN 1 ELSE 0 END) AS signup,
    MAX(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS add_to_cart,
    MAX(CASE WHEN event_type = 'purchase'   THEN 1 ELSE 0 END) AS purchase
FROM events_cleaned
GROUP BY session_id, user_id;

-- ============================================
-- 2. Funnel counts and conversion rates
-- ============================================
WITH funnel_counts AS (
    SELECT
        SUM(visit)       AS visits,
        SUM(signup)      AS signups,
        SUM(add_to_cart) AS add_to_cart,
        SUM(purchase)    AS purchases
    FROM funnel_sessions
)
SELECT
    visits,
    signups,
    add_to_cart,
    purchases,
    ROUND(100.0 * signups       / NULLIF(visits, 0), 2)    AS signup_rate_pct,
    ROUND(100.0 * add_to_cart   / NULLIF(visits, 0), 2)    AS add_to_cart_rate_pct,
    ROUND(100.0 * purchases     / NULLIF(visits, 0), 2)    AS overall_conversion_pct,
    ROUND(100.0 * purchases     / NULLIF(add_to_cart, 0), 2) AS cart_to_purchase_pct
FROM funnel_counts;

-- ============================================
-- 3. Funnel by device
-- ============================================
WITH session_device AS (
    SELECT session_id, device
    FROM events_cleaned
    GROUP BY session_id, device
),
funnel_device AS (
    SELECT
        sd.device,
        SUM(f.visit)       AS visits,
        SUM(f.signup)      AS signups,
        SUM(f.add_to_cart) AS add_to_cart,
        SUM(f.purchase)    AS purchases
    FROM funnel_sessions f
    JOIN session_device sd ON f.session_id = sd.session_id
    GROUP BY sd.device
)
SELECT
    device,
    visits,
    signups,
    add_to_cart,
    purchases,
    ROUND(100.0 * purchases / NULLIF(visits, 0), 2) AS conversion_pct
FROM funnel_device
ORDER BY visits DESC;

-- ============================================
-- 4. KPIs: Revenue, AOV, Orders
-- ============================================
-- Assumes events_cleaned has purchase events with product_id/quantity
-- and products table has price.
SELECT
    COUNT(DISTINCT session_id) AS total_orders,
    SUM(quantity * price)     AS total_revenue,
    ROUND(AVG(order_value), 2) AS avg_order_value
FROM (
    SELECT
        e.session_id,
        e.product_id,
        e.quantity,
        p.price,
        e.quantity * p.price AS order_value
    FROM events_cleaned e
    JOIN products_cleaned p ON e.product_id = p.product_id
    WHERE e.event_type = 'purchase'
) orders;

-- ============================================
-- 5. Top products by revenue
-- ============================================
SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(e.quantity) AS units_sold,
    SUM(e.quantity * p.price) AS revenue
FROM events_cleaned e
JOIN products_cleaned p ON e.product_id = p.product_id
WHERE e.event_type = 'purchase'
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 20;

-- ============================================
-- 6. Daily conversion rate (time series)
-- ============================================
WITH daily_funnel AS (
    SELECT
        DATE(timestamp) AS date,
        COUNT(DISTINCT CASE WHEN event_type = 'visit'       THEN session_id END) AS visits,
        COUNT(DISTINCT CASE WHEN event_type = 'purchase'    THEN session_id END) AS purchases
    FROM events_cleaned
    GROUP BY DATE(timestamp)
)
SELECT
    date,
    visits,
    purchases,
    ROUND(100.0 * purchases / NULLIF(visits, 0), 2) AS conversion_pct
FROM daily_funnel
ORDER BY date;
