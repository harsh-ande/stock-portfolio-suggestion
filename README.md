
# **Stock Portfolio Suggestion Engine**

## **Overview**
The Stock Portfolio Suggestion Engine is a Python-based application designed to assist users in creating personalized stock portfolios based on their investment preferences. Users can input a dollar amount, select one or two investment strategies, and receive optimized portfolio suggestions mapped to stocks or ETFs. 

---

## **Features**
- **Investment Strategies**:
  - Ethical Investing, Growth Investing, Index Investing, Quality Investing, Value Investing.
- **Portfolio Allocation**:
  - Dynamic allocation based on user input and predefined strategy mappings.
- **Real-Time Data**:
  - Fetches up-to-date stock/ETF prices.
  - Tracks and visualizes 5-day portfolio trends.
- **User-Friendly Interface**:
  - Interactive UI with portfolio insights and real-time monitoring.

---

## **Getting Started**

### **Prerequisites**
- Python 3.7+
- Required Libraries: `pandas`, `numpy`, `matplotlib`, `yfinance`, `flask` or `streamlit`, `plotly`.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/harsh-ande/stock-portfolio-suggestion.git
   cd stock-portfolio-suggestion
   ```
2. Run the application:
   - Flask UI:
     ```bash
     python app.py
     ```
   - Streamlit UI:
     ```bash
     streamlit run app.py
     ```

---

## **Usage**
1. **Input Details**:
   - Enter investment amount (minimum $5000).
   - Select one or two investment strategies.
2. **View Suggestions**:
   - Suggested stocks/ETFs mapped to selected strategies.
   - Allocation of investment across assets.
3. **Monitor Performance**:
   - Real-time portfolio value updates.
   - Visualize 5-day historical trends.

---

## **Project Details**
- **Investment Strategy Mapping**:
  - Example: **Index Investing** maps to VTI, IXUS, ILTB; **Ethical Investing** maps to AAPL, ADBE, NSRGY.
- **Allocation Logic**:
  - Proportional division of investment amount among selected assets.
- **Visualization**:
  - Weekly portfolio trends via `matplotlib` or `plotly`.
- **Data Source**:
  - Real-time stock/ETF prices from the `yfinance` API.

---

## **Additional Resources**
- **Presentation Slides**: [Google Slides](https://docs.google.com/presentation/d/1crcFx46Im-dg5MYOpxmHWAB4QeHpHaL-EFQKVCabkvg/edit?usp=sharing)
- **Video Presentation**: [Google Drive](https://drive.google.com/file/d/1gEbO-AUxpT36W9g79JdyC3gwDQ81Aq-c/view)

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

--- 
