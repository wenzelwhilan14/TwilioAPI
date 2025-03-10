from twilio.rest import Client
from src.config.settings import Config

client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

def make_call(to, message):
    """ Realiza una llamada y lee un mensaje en voz alta """
    try:
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            from_=Config.TWILIO_PHONE_NUMBER,
            to=to
        )
        return call.sid
    except Exception as e:
        raise Exception(f"Error al hacer la llamada: {str(e)}")

def send_sms(to, message):
    """ Envía un SMS con Twilio """
    try:
        sms = client.messages.create(
            body=message,
            from_=Config.TWILIO_PHONE_NUMBER,
            to=to
        )
        return sms.sid
    except Exception as e:
        raise Exception(f"Error al enviar SMS: {str(e)}")
