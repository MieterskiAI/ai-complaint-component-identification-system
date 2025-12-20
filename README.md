# AI-Assisted Complaint & Component Identification System

## Project Overview
This project demonstrates an AI-assisted decision-support system designed to help operational teams identify potentially relevant components during product complaint handling.

The system does not automate decisions. Instead, it uses AI to eliminate incorrect component paths and provide structured reasoning, while keeping the final responsibility fully in human hands.

Google Sheets serves as the single source of truth for orders, deliveries, components, and complaints, while Zapier orchestrates the end-to-end process.

## Business Problem
In many operational environments, product complaints require fast identification of the correct replacement component.

Incomplete information, fragmented data sources, and time pressure often lead to incorrect component selection. This results in unnecessary logistics costs, extended resolution times, and repeated service cycles.

The problem is not a lack of data, but the lack of structured decision support that helps eliminate incorrect options before a final human decision is made.

## Solution Concept
The system is designed as a lightweight decision-support layer on top of existing operational data.

Instead of replacing human judgment, it focuses on structuring available information and eliminating incompatible component options based on order details, delivery data, and component compatibility rules.

AI is used exclusively to analyze context and narrow down possible components, providing reasoning that supports faster and more accurate human decisions.

## System Architecture
### Data Layer
Google Sheets is used as the single source of truth, storing structured data for orders, delivered products, components, and complaints. Each dataset is separated into dedicated sheets to ensure clarity and traceability.

### Automation Layer
Zapier orchestrates the end-to-end workflow, reacting to complaint entries, retrieving related order and delivery data, and coordinating AI analysis without manual intervention.

### AI Layer
AI is integrated as an analytical component responsible for eliminating incompatible components and generating structured reasoning. It does not make final decisions or trigger downstream actions autonomously.

## End-to-End Process Flow

## Role of AI vs Human

## Example Case

## Why This Design Is Safe and Realistic

## What This Project Is Not
