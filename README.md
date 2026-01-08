# Complaint & Component Identification – Decision-Support System for After-Sales Operations

Designing human-centered workflows that support accurate component selection during product complaint handling.

## 🧠 Business Context

In after-sales operations, product complaints often require fast and precise identification of replacement components.  
Time pressure, fragmented data sources and incomplete information lead to wrong decisions, repeated logistics cycles and increased operational costs.

This project is not about automating responsibility.

It is about designing a decision-support workflow that helps employees:
- understand the real context of each complaint,
- eliminate incompatible component options,
- and make confident final decisions.

## 🔁 Before / After

**Before**
- manual complaint triage  
- high risk of selecting wrong components  
- repeated logistics cycles  
- operational knowledge locked in individuals  

**After**
- structured elimination of incompatible components  
- transparent reasoning for every suggestion  
- faster resolution time  
- reduced operational uncertainty  

## 🔄 Decision Flow

Complaint Entry  
→ Context & Data Retrieval  
→ AI Elimination of Incompatible Components  
→ Suggested Options + Reasoning  
→ Human Final Decision

## 🤝 Human-in-the-Loop

This system never selects or dispatches components automatically.  
AI narrows down possible options and provides structured reasoning, but the final responsibility always remains with the human operator.

---

## How the Pipeline Works

**1. Complaint Registration**  
A complaint is registered in the Complaints sheet and marked as ready for analysis.

**2. Context Retrieval**  
The automation retrieves related order, delivery and product data based on Order ID.

**3. Component Candidate Retrieval**  
All potentially compatible components are loaded from the reference dataset.

**4. AI Analysis**  
AI analyzes complaint description and structured data to eliminate incompatible components.

**5. Suggested Options + Reasoning**  
One or two most likely components are proposed together with clear reasoning.

**6. Human Review**  
The AI-generated context is written back to the complaint record for final human decision.

---

## ⚡ Why This Project Matters

After-sales teams operate under constant pressure to resolve complaints quickly and accurately.

This system supports operational decision making by:
- reducing the risk of incorrect component selection  
- shortening resolution cycles  
- lowering logistics and re-dispatch costs  
- making decision logic transparent and auditable  

Perfect for:
- customer support  
- technical service teams  
- warranty and repair departments  
- manufacturing companies  

---

## 📌 Future Improvements

- integration with ERP / CRM systems  
- automated detection of missing complaint data  
- advanced compatibility rules  
- multi-language complaint analysis  

---

## 👤 Author

**MieterskiAI**  
Junior AI Process & Decision Support Designer — designing human-centered AI workflows that help organizations regain control over complex operational processes.

---

## ⭐ Support

If this project was helpful, leave a ⭐ on GitHub.
