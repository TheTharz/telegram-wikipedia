# Telegram Wikipedia Bot 🤖

A simple and efficient Telegram bot that provides Wikipedia summaries on demand. Search for any topic and get instant Wikipedia summaries directly in your Telegram chat!

## Features

- 📖 **Wikipedia Search**: Get concise summaries of Wikipedia articles
- 🔍 **Smart Disambiguation**: Handles ambiguous search terms with suggestions
- 🚀 **Fast & Reliable**: Built with modern Python async/await patterns
- 🌍 **Multi-language Support**: Configurable Wikipedia language (default: English)

## Commands

- `/start` - Welcome message and bot introduction
- `/help` - Display help menu with available commands
- `/wiki <search term>` - Search Wikipedia and get a summary
- Any other text - Bot will echo it back

## Installation

### Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (obtain from [@BotFather](https://t.me/botfather))

### Setup

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd telegram-bot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv telegram_bot_env
   source telegram_bot_env/bin/activate  # On Windows: telegram_bot_env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:

   ```env
   BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_HERE
   ```

5. **Run the bot**
   ```bash
   python bot.py
   ```

## Getting a Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Start a chat and send `/newbot`
3. Follow the instructions to create your bot
4. Copy the token and add it to your `.env` file

## Usage Examples

### Basic Wikipedia Search

```
User: /wiki Python programming
Bot: 📖 Python programming

Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected.
```

### Handling Ambiguous Terms

```
User: /wiki Mercury
Bot: That term is ambiguous. Try one of these:
• Mercury (planet)
• Mercury (element)
• Mercury (mythology)
• Mercury (automobile)
• Mercury Records
```

### Echo Function

```
User: Hello there!
Bot: You said: Hello there!
```

## Project Structure

```
telegram-bot/
├── bot.py              # Main bot application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .env               # Environment variables (create this)
└── telegram_bot_env/  # Virtual environment
```

## Dependencies

- **python-telegram-bot** (22.3) - Telegram Bot API wrapper
- **wikipedia** (1.4.0) - Wikipedia API client
- **python-dotenv** (1.1.1) - Environment variable management
- **httpx** (0.28.1) - HTTP client for async requests
- Additional networking and utility packages

## Configuration

You can modify the bot's behavior by editing `bot.py`:

- **Language**: Change `wikipedia.set_lang("en")` to your preferred language code
- **Summary Length**: Modify `sentences=3` in the wiki_search function
- **Bot Messages**: Customize response messages and help text

## Error Handling

The bot includes comprehensive error handling for:

- Missing search terms
- Ambiguous Wikipedia pages
- Non-existent pages
- Network connectivity issues
- Unexpected errors

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Bot doesn't respond**

- Check if your bot token is correct in the `.env` file
- Ensure the bot is running (`python bot.py` should show "Bot is running...")
- Verify your internet connection

**Wikipedia searches fail**

- Check your internet connection
- Try different search terms
- The Wikipedia API might be temporarily unavailable

**Import errors**

- Make sure you've activated the virtual environment
- Run `pip install -r requirements.txt` to ensure all dependencies are installed

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Excellent Telegram Bot API wrapper
- [Wikipedia Python Library](https://github.com/goldsmith/Wikipedia) - Simple Wikipedia API access
- [Telegram Bot API](https://core.telegram.org/bots/api) - Official Telegram Bot documentation

---

**Made with ❤️ for the Telegram community**

For questions or support, feel free to open an issue on GitHub!
