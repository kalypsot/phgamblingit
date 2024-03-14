# Define a handler for the /start command
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome, {user.first_name}! You have received a Free Token of 10 pesos added to your balance.")

    # Add the Free Token amount to the user's balance (this is a placeholder)
    # Here you would implement logic to update the user's balance in your system

# Set up the Telegram Bot token and dispatcher
updater = Updater(6782072967:AAGuG_authp9yj3RSeIeIpk_kYZhhwP-jwo")
dispatcher = updater.dispatcher

# Add a handler for the /start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the Bot
updater.start_polling()
updater.idle()
