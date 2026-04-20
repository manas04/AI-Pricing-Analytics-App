import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px


st.set_page_config(page_title="AI Pricing Analytics", layout="wide")
st.title("AI Pricing Analytics App")

# File Upload (taking csv as an input)
upload_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if upload_file:
    df = pd.read_csv(upload_file)

    if "price" in df.columns and "cogs" in df.columns:
        df["unit_margin"] = df["price"] - df["cogs"]

    if "unit_margin" in df.columns and "units_sold" in df.columns:
        df["profit"] = df["unit_margin"]* df["units_sold"]

    # Data Preview-------------------
    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

   # KPIs-----------------------------
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    if "revenue" in df.columns:
        col1.metric("Total Revenue", f"${df['revenue'].sum():,.0f}")
    else:
        col1.metric("Total Revenue", "N/A")

    
    if "units_sold" in df.columns:
        col2.metric("Total Units Sold",f"{df['units_sold'].sum():,.0f}")
    else:
        col2.metric("Total Units Sold", "N/A")
    

    if "price" in df.columns:
        col3.metric("Avg Price", f"${df['price'].mean():.2f}")
    else:
        col3.metric("Avg Price", "N/A")

    col4, col5, col6 = st.columns(3)

    if "cogs" in df.columns:
        col4.metric("Avg COGS", f"${df['cogs'].mean():.2f}")
    else:
        col4.metric("Avg COGS", "N/A")

    if "unit_margin" in df.columns:
        col5.metric("Avg Unit Margin", f"${df['unit_margin'].mean():.2f}")
    else:
        col5.metric("Avg Unit Margin", "N/A")

    if "profit" in df.columns:
        col6.metric("Total Profit", f"${df['profit'].sum():,.0f}")
    else:
        col6.metric("Total Profit", "N/A")

    col7, col8, col9 = st.columns(3)

    if "competitor_price" in df.columns:
        col7.metric("Avg Competitor Price", f"${df['competitor_price'].mean():.2f}")
    else:
        col7.metric("Avg Competitor Price", "N/A")

    if "inventory" in df.columns:
        col8.metric("Total Inventory", f"{df['inventory'].sum():,.0f}")
    else:
        col8.metric("Total Inventory", "N/A")

    if "promo_flag" in df.columns:
        promo_share = df["promo_flag"].mean() * 100
        col9.metric("Promo Share", f"{promo_share:.1f}%")
    else:
        col9.metric("Promo Share", "N/A")

    # Elasticity section ---------------------
    st.subheader("Price Elasticity Analysis")
    required_cols = {"product_id", "price", "units_sold"}
    if required_cols.issubset(df.columns):
        product_list = df["product_id"].dropna().unique()
        selected_product = st.selectbox("Select Product", sorted(product_list))
        product_df = df[df["product_id"] == selected_product].copy()

        # Keep only valid rows
        product_df = product_df[(product_df["price"]>0) & (product_df["units_sold"]>0)]

        if len(product_df) >= 2:
            product_df["log_price"] = np.log(product_df["price"])
            product_df["log_units"] = np.log(product_df["units_sold"])

            X = product_df[["log_price"]]
            y = product_df["log_units"]

            model = LinearRegression()
            model.fit(X, y)

            elasticity = model.coef_[0]
            r2 = model.score(X, y)

            col1, col2 = st.columns(2)
            col1.metric("Estimated Elasticity", f"{elasticity:.2f}")
            col2.metric("Model R²", f"{r2:.2f}")

            if elasticity < -1:
                st.success("Demand appears elastic. Price changes likely have a strong impact on units sold.")
            elif -1 <= elasticity < 0:
                st.info("Demand appears inelastic. Price changes likely have a smaller impact on units sold.")
            else:
                st.warning("Elasticity is zero or positive. This may indicate noisy data, promotions, or other factors influencing demand.")

            fig = px.scatter(
                product_df,
                x="price",
                y="units_sold",
                title=f"Price vs Units Sold for Product {selected_product}",
                trendline="ols"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(product_df[["date", "product_id", "price", "units_sold"]])
        else:
            st.warning("Not enough valid data points for elasticity analysis.")
    else:
        st.warning("Dataset must include product_id, price, and units_sold columns.")
    
    # Scenario Simulator --------------------------------------------------------
    st.subheader("Pricing Scenario Simulator")
    if required_cols.issubset(df.columns):

        selected_product = st.selectbox(
            "Select Product for Simulation",
            sorted(df["product_id"].dropna().unique()),
            key="sim_product"
        )

        product_df = df[df["product_id"] == selected_product]

        if len(product_df) > 0:

            avg_price = product_df["price"].mean()
            avg_units = product_df["units_sold"].mean()
            avg_cogs = product_df["cogs"].mean() if "cogs" in df.columns else 0

            st.write(f"Current Avg Price: ${avg_price:.2f}")
            st.write(f"Current Avg Units Sold: {avg_units:.0f}")

            # User input
            price_change_pct = st.slider(
                "Change Price (%)",
                min_value=-30,
                max_value=30,
                value=0
            )

            new_price = avg_price * (1 + price_change_pct / 100)

            # Use elasticity from earlier model
            if 'elasticity' in locals():

                new_units = avg_units * (1 + elasticity * (price_change_pct / 100))

                new_revenue = new_price * new_units
                new_profit = (new_price - avg_cogs) * new_units

                col1, col2, col3 = st.columns(3)

                col1.metric("New Price", f"${new_price:.2f}")
                col2.metric("Estimated Units", f"{new_units:.0f}")
                col3.metric("Estimated Revenue", f"${new_revenue:,.0f}")

                col4, col5 = st.columns(2)
                col4.metric("Estimated Profit", f"${new_profit:,.0f}")

                if new_revenue > avg_price * avg_units:
                    st.success("This price change may increase revenue.")
                else:
                    st.warning("This price change may reduce revenue.")

            else:
                st.warning("Run elasticity analysis first.")




