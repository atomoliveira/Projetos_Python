#Faça programa que teste a velocidade de rede de casa 

import speedtest

def testar_velocidade():
    try:
        st = speedtest.Speedtest()  # Usando Speedtest com "S" maiúsculo
        print("Iniciando teste de velocidade...")
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convertendo bits para megabits
        upload_speed = st.upload() / 1_000_000  # Convertendo bits para megabits
        print(f"Velocidade de download: {download_speed:.2f} Mbps")
        print(f"Velocidade de upload: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    testar_velocidade()
