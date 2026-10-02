from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa de vendas: ")

    control.create_leads(model_lead(name, email, stage))

def list_leads():
    leads = control.read_leads()
    
    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<12} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()

    found_leads = control.read_leads_search(query)

    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in found_leads:
        print(f"{i:02d} | {lead["name"]:<12} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar")
    else:
        print(f"CSV exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()