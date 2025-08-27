# Customer Support Chatbot 🤖

A simple yet powerful customer support chatbot built with Python, Streamlit, and OpenAI's GPT-3.5 API. This application provides an intuitive web interface for customer interactions and automatically logs all conversations to CSV files.

## Features

- **Web-based Interface**: Clean, user-friendly Streamlit UI
- **OpenAI Integration**: Powered by GPT-3.5-turbo for intelligent responses
- **Chat Logging**: Automatic conversation logging to CSV files
- **Session Management**: Unique session IDs for tracking conversations
- **Download Logs**: Export chat history for analysis
- **Professional Responses**: Optimized for customer support scenarios

## Setup Instructions

### Prerequisites
- Python 3.7+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd customer-support-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run chatbot.py
   ```

4. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Enter your OpenAI API key in the sidebar
   - Start chatting!

## Usage

1. **Start the Application**: Run `streamlit run chatbot.py`
2. **Enter API Key**: Input your OpenAI API key in the sidebar
3. **Chat**: Type messages in the chat input at the bottom
4. **View History**: All messages are displayed in the main chat area
5. **Clear Chat**: Use the "Clear Chat" button to start fresh
6. **Download Logs**: Export conversation history as CSV

## File Structure

```
customer-support-chatbot/
│
├── chatbot.py          # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── chat_logs.csv      # Generated chat logs (created automatically)
```

## Configuration

The chatbot comes with a built-in system prompt optimized for customer support:
- Polite and professional tone
- Helpful problem-solving approach
- Graceful handling of complex issues
- Directs users to human support when needed

You can modify the system prompt in the `CustomerSupportChatbot` class.

## Chat Logging

All conversations are automatically logged to `chat_logs.csv` with the following structure:
- `timestamp`: When the message was sent
- `session_id`: Unique identifier for the chat session
- `role`: Either "user" or "assistant"
- `message`: The actual message content

## Customization Ideas

- **Add authentication**: Implement user login system
- **Database integration**: Store logs in SQLite or PostgreSQL
- **Multiple language support**: Add translation capabilities
- **Sentiment analysis**: Track customer satisfaction
- **Integration**: Connect with CRM systems or helpdesk tools

## Security Notes

- Never commit your OpenAI API key to version control
- Consider using environment variables for production deployment
- Implement rate limiting for production use
- Review chat logs for sensitive information before sharing

## Troubleshooting

**Common Issues:**

1. **"Please enter your OpenAI API key"**
   - Make sure you've entered a valid OpenAI API key in the sidebar

2. **Connection errors**
   - Check your internet connection
   - Verify your API key is active and has credits

3. **Import errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue on GitHub or contact the maintainer.

---

**Happy chatting!** 🚀
