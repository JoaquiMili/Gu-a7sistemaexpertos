# Sistema Experto Basado en Reglas para diagnóstico de fallas de red

# Reglas SI–ENTONCES
rules = [
    {
        "conditions": ["no_conexion", "router_apagado"],
        "conclusion": "Encender router"
    },
    {
        "conditions": ["no_conexion", "router_encendido", "ping_falla"],
        "conclusion": "Revisar cable de red"
    },
    {
        "conditions": ["no_conexion", "ping_ok"],
        "conclusion": "Verificar configuración IP"
    },
    {
        "conditions": ["navegacion_lenta", "muchos_dispositivos"],
        "conclusion": "Reducir uso simultáneo de red"
    },
    {
        "conditions": ["navegacion_lenta", "pocos_dispositivos", "velocidad_baja"],
        "conclusion": "Contactar proveedor de Internet"
    },
    {
        "conditions": ["wifi_debil"],
        "conclusion": "Acercar equipo al router o cambiar canal Wi-Fi"
    },
    {
        "conditions": ["conexion_inestable", "ip_dinamica"],
        "conclusion": "Revisar servidor DHCP"
    },
    {
        "conditions": ["conexion_inestable", "switch_falla"],
        "conclusion": "Reiniciar switch o router"
    },
    {
        "conditions": ["no_imprime", "impresora_apagada"],
        "conclusion": "Encender impresora"
    },
    {
        "conditions": ["no_imprime", "impresora_encendida", "ip_incorrecta"],
        "conclusion": "Asignar IP correcta a impresora"
    },
    {
        "conditions": ["ping_impresora_falla", "impresora_encendida"],
        "conclusion": "Revisar conexión de red de la impresora"
    },
    {
        "conditions": ["sin_conexion_total"],
        "conclusion": "Revisar conexión WAN o cableado troncal"
    }
]

def diagnosticar(sintomas_usuario):
    diagnosticos = []
    reglas_activadas = []
    for regla in rules:
        if all(cond in sintomas_usuario for cond in regla["conditions"]):
            diagnosticos.append(regla["conclusion"])
            reglas_activadas.append(regla)
    return diagnosticos, reglas_activadas

# === Casos de prueba ===

casos_de_prueba = {
    "Caso 1": ["no_conexion", "router_apagado"],
    "Caso 2": ["no_conexion", "router_encendido", "ping_falla"],
    "Caso 3": ["navegacion_lenta", "muchos_dispositivos"],
    "Caso 4": ["wifi_debil"],
    "Caso 5": ["no_imprime", "impresora_encendida", "ip_incorrecta"]
}

# === Ejecución de los casos de prueba ===
for nombre, sintomas in casos_de_prueba.items():
    print(f"\n🔎 {nombre}")
    print(f"Síntomas ingresados: {sintomas}")
    diagnostico, reglas = diagnosticar(sintomas)
    if diagnostico:
        print("✅ Diagnóstico:")
        for d in diagnostico:
            print(f" - {d}")
        print("📌 Reglas activadas:")
        for r in reglas:
            print(f"  SI {' Y '.join(r['conditions'])} ENTONCES {r['conclusion']}")
    else:
        print("⚠️ No se pudo determinar un diagnóstico con los síntomas ingresados.")
