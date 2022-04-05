from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

## Init Flask APp
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
  ## GEt user message
    user_msg = request.values.get('Body', '').lower()
    ## Init bot response
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    # Applying bot logic
    if 'ola' in user_msg:
        msg.body("Olá, como vai? Bem-vindo ao Unit Carreiras! Para que a gente possa te ajudar, informe se você é um aluno (escreva aluno no chat), uma empresa (escreva empresa no chat) ou Agente de Integração (digite integração no chat")
    elif 'aluno' in user_msg:
        msg.body("Olá aluno, em que podemos te ajudar? Digite conforme a opção correspondente:")
        msg.body('a1 para entrega de documentação referente ao estágio, a2 para acordo de cooperação, a3 para vagas, a4 para crendencial de estágio, a5 para declaração de realização de estágio ou a6 p/ outras dúvidas')
    elif 'a1' in user_msg:
        msg.body("É necessário abrir um protocolo no magister de “Documentação de estágio não obrigatório” com os anexos para que possamos analisar e assinar ou pode ser entregue presencialmente no Bloco A, sala 01")
    elif 'a2' in user_msg:
        msg.body("Para solicitar o Acordo de Cooperação, favor entrar em contato  através do email carreiras@unit.br, informando “Solicitação de Acordo de Cooperação” o nome da empresa, telefone e email da empresa.")
    elif 'a3' in user_msg:
        msg.body("Para acessar as vagas é necessário abrir o Magister WEB e entrar na página do carreiras (ícone amarelo) e em seguida clique em “vagas de estágio”. Lá estarão todas as vagas disponíveis e informações necessárias para candidatura. Fique atento ao email, pois sempre divulgamos vagas de estágio ao email “souunit”.")
    elif 'a4' in user_msg:
        msg.body("É necessário abrir um protocolo no magister de “Documentação de estágio não obrigatório” com os anexos para que possamos analisar e assinar ou pode ser entregue presencialmente no Bloco A, sala 01")
    elif 'a5' in user_msg:
        msg.body("Declaração de Realização de Estágio é um comprovante no qual é informado a situação atual ou passada do estagiário é um documento em que informamos o período que o aluno realizou estágio extracurricular. ")
        msg.body("Tal declaração é utilizada para aproveitamentos da carga horária para atividades complementares e é confeccionada principalmente quando o Contrato de estágio não é localizado pelo aluno. ")
        msg.body("Para ser confeccionado o aluno precisa estar com a documentação em dia (entrega de relatório, termo aditivo, rescisão de contrato) e informando no campo de observações local qual estagiou, vigência do contrato e 03 atividades qual exercia dentro da empresa qual possuía vínculo.")
    elif 'a6' in user_msg:
        msg.body("Para demais dúvidas, digite que iremos responder ou entre em contato através do nosso número (79) 3218-2113, ou nos encontre no Bloco A, sala 01, referência: fundo do Gelo e Açúcar.")
    elif 'empresa' in user_msg:
        msg.body("Olá empresa, em que podemos te ajudar? Digite conforme a opção correspondente:")
        msg.body('e1 para entrega de documentação do estágio, e2 para acordo de cooperação, e3 para vagas, e4 para outras dúvidas')
    elif 'e1' in user_msg:
        msg.body("A entrega das documentações será por e-mail!")
    elif 'e2' in user_msg:
        msg.body("Informe o procedimento pelo e-mail carreiras@unit.br")
    elif 'e3' in user_msg:
        msg.body("Veja aqui o tutorial de como ver as vagas: www.videotutorial.loremipsum")
    elif 'e4' in user_msg:
        msg.body("Informe sua dúvida, preferencialmente em uma só mensagem, que logo logo estaremos entrando em contato. Unit Carreiras agradece!")
    elif 'empresa' in user_msg:
        msg.body("Olá Agente de Integração, em que podemos te ajudar? Digite conforme a opção correspondente:")
        msg.body('i1 para entrega de documentação do estágio, i2 para acordo de cooperação, i3 para vagas, i4 para outras dúvidas')
    elif 'i1' in user_msg:
        msg.body("A entrega das documentações será por e-mail!")
    elif 'i2' in user_msg:
        msg.body("Informe o procedimento pelo e-mail carreiras@unit.br")
    elif 'i3' in user_msg:
        msg.body("Veja aqui o tutorial de como ver as vagas: www.videotutorial.loremipsum")
    elif 'i4' in user_msg:
        msg.body("Informe sua dúvida, preferencialmente em uma só mensagem, que logo logo estaremos entrando em contato. Unit Carreiras agradece!")
    elif 'senhormicha' in user_msg:
        msg.body('eh brabo')
    elif 'gatos' in user_msg:
        msg.media('gatos são fofos, é sobre isso rsrs https://cataas.com/cat')
    else:
        msg.body("A opção que você digitou é inválida! Digite corretamente a opção correspondente a o que você deseja. Lembre-se de digitar com a letra minúscula!")
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)