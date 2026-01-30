# Binance Futures Testnet Trading Bot (CLI)

A Python-based command-line trading bot for **Binance Futures Testnet (USDT-M)**.
This application allows users to place **Market** and **Limit** orders using a clean, modular, and reusable architecture with proper logging, validation, and error handling.

This project is built as part of a technical assignment for the **Junior Python Developer** role.

---

## Objective

Build a small Python application that can place orders on **Binance Futures Testnet (USDT-M)** and provide:

* Clean reusable structure
* Proper logging
* Error handling
* CLI-based interaction
* Professional project architecture

---

## Features

* Place **Market** orders
* Place **Limit** orders
* Supports both **BUY** and **SELL** sides
* Binance Futures **Testnet (Demo)** integration
* Command-line interface (CLI)
* Input validation
* Structured project architecture
* Logging of API requests, responses, and errors
* Exception handling (invalid input, API errors, network failures)

---

## Tech Stack

* Python 3.x
* python-binance
* python-dotenv
* argparse
* Binance Futures Testnet (Demo)

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py        # Binance API client wrapper
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   └── logging_config.py# Logging configuration
│
├── cli.py               # CLI entry point
├── README.md
├── requirements.txt
├── .env                 # API keys (not committed)
└── logs/
    └── trading.log
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd trading_bot
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_demo_api_key
BINANCE_SECRET_KEY=your_demo_secret_key
```

> Note: These must be **Binance Demo/Testnet API keys**, not real Binance API keys.

---

## How to Run

### Market Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

---

## CLI Output

The CLI prints:

* Order request summary
* Order response details
* Order ID
* Order status
* Executed quantity
* Average price (if available)
* Success/failure message

---

## Logs

All API requests, responses, and errors are logged in:

```
logs/trading.log
```

Log file contains:

* One MARKET order log
* One LIMIT order log
* API responses
* Error traces (if any)

---

## Validation & Error Handling

The application validates:

* Symbol
* Order side (BUY/SELL)
* Order type (MARKET/LIMIT)
* Quantity
* Price (required for LIMIT orders)

Handles:

* Invalid user input
* API errors
* Network failures
* Missing configuration

---

## Assumptions

* Orders are executed on **Binance Futures Testnet (Demo)** only
* No real funds are used
* API keys are stored securely using environment variables
* USDT-M futures symbols are used (e.g., BTCUSDT)

---

## Architecture Notes

This project follows a layered architecture:

* API Layer → `client.py`
* Business Logic Layer → `orders.py`
* Validation Layer → `validators.py`
* Logging Layer → `logging_config.py`
* Interface Layer → `cli.py`

This separation ensures:

* Maintainability
* Scalability
* Testability
* Clean code structure

---

## Deliverables Included

* Source code
* README.md
* requirements.txt
* logs/trading.log
* CLI interface
* Structured project architecture

---



