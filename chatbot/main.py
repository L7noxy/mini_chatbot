import random
import nltk
from nltk.chat.util import Chat, reflections

# Baixar recursos necessários do NLTK
nltk.download('punkt')

# Padrões de conversa e respostas
pares = [
    [
        r"oi|olá|e aí",
        ["Olá! Como posso ajudar você hoje?", "Oi! Tudo bem?", "E aí! Como vai?"]
    ],
    [
        r"qual é o seu nome?",
        ["Eu sou um chatbot. Pode me chamar de Bot!", "Meu nome é Chatbot. E o seu?"]
    ],
    [
        r"como você está?",
        ["Estou bem, obrigado por perguntar!", "Tudo ótimo! E você?"]
    ],
    [
        r"qual é o seu propósito?",
        ["Meu propósito é ajudar você com suas dúvidas e conversar!", "Eu existo para tornar sua vida um pouco mais fácil."]
    ],
    [
        r"quem criou você?",
        ["Fui criado por um desenvolvedor usando Python e NLTK!", "Um programador me trouxe à vida."]
    ],
    [
        r"tchau|adeus|sair",
        ["Tchau! Até a próxima.", "Foi bom conversar com você. Adeus!"]
    ],
    [
        r"meu nome é (.*)",
        ["Prazer em conhecê-lo, %1! Como posso ajudar?", "Oi, %1! Tudo bem?"]
    ],
    [
        r"você gosta de (.*)?",
        ["Ah, %1 é interessante! Mas sou apenas um bot, então não tenho preferências.", "Não tenho opiniões, mas %1 parece legal!"]
    ],
    [
        r"o que você pode fazer?",
        ["Posso conversar com você, responder perguntas simples e tentar ajudar no que for possível!", "Sou um chatbot, então posso conversar e tentar ajudar com suas dúvidas."]
    ],
    [
        r"(.*) (ajuda|socorro)",
        ["Claro! Posso tentar ajudar. O que você precisa?", "Estou aqui para ajudar. Conte-me mais."]
    ],
    [
        r"(.*)",
        ["Desculpe, não entendi. Pode repetir?", "Não tenho certeza do que você quer dizer. Pode explicar melhor?"]
    ]
]

# Criar o chatbot
chatbot = Chat(pares, reflections)

def iniciar_chat():
    print("Olá! Eu sou um chatbot mais avançado. Como posso ajudar você hoje?")
    while True:
        try:
            user_input = input("Você: ")
            if user_input.lower() in ["tchau", "adeus", "sair"]:
                print("Chatbot: Tchau! Até a próxima.")
                break
            resposta = chatbot.respond(user_input)
            print(f"Chatbot: {resposta}")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Até logo!")
            break

if __name__ == "__main__":
    iniciar_chat()