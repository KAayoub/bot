from telegram.ext import Updater, MessageHandler, Filters
TOKEN = '8131202922:AAH2TvegSoedW-I2d8qLU-GX3WNKaf-epRo'
def reply(update, context):
    text = update.message.text.lower().strip()
    if "what should i eat" in text and "1/15/2026" in text:
        answer = (
            "🍳 Breakfast\n"
            "Two cheese & egg burgers\n"
            "Milk shake with banana, oats, and peanut butter\n\n"
            "🍝 Lunch\n"
            "Pasta with cheese, liver, and bread\n\n"
            "🥤 Snack\n"
            "Milk, yogurt, banana, and honey shake\n\n"
            "🌙 Dinner\n"
            "Liver, pasta, bread, and cheese\n\n"
            "💧 Drink 3 liters of water per day"
        )
    elif "what should i eat" in text and "1/16/2026" in text:
        answer = (
            "🍳 Breakfast\n"
            "Two cheese & egg burgers\n"
            "Milk shake with banana, oats, and peanut butter\n\n"
            "🍝 Lunch\n"
            "Rice with cheese, potatoes, corn, and minced meat\n\n"
            "🥤 Snack\n"
            "Milk, yogurt, banana, and honey shake\n\n"
            "🌙 Dinner\n"
            "Rice with cheese, potatoes, corn, and minced meat\n\n"
            "💧 Drink 3 liters of water per day"
        )
    else:
        answer = (
            "❓ Please type:\n"
            "What should I eat on 1/15/2026\n"
            "or\n"
            "What should I eat on 1/16/2026"
        )
    update.message.reply_text(answer)
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
