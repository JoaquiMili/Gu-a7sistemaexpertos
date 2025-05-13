# === Sistema experto con prioridad en reglas ===

rules = [
    {"conditions": ["no_conexion", "router_apagado"], "conclusion": "Encender router", "prioridad": 5},
    {"conditions": ["no_conexion", "router_encendido", "ping_falla"], "conclusion": "Revisar cable de red", "prioridad": 5},
    {"conditions": ["no_conexion", "ping_ok"], "conclusion": "Verificar configuración IP", "prioridad": 4},
    {"conditions": ["navegacion_lenta", "muchos_dispositivos"], "conclusion": "Reducir uso simultáneo de red", "prioridad": 2},
    {"conditions": ["navegacion_lenta", "pocos_dispositivos", "velocidad_baja"], "conclusion": "Contactar proveedor de Internet", "prioridad": 3},
    {"conditions": ["wifi_debil"], "conclusion": "Acercar equipo al router o cambiar canal Wi-Fi", "prioridad": 2},
    {"conditions": ["conexion_inestable", "ip_dinamica"], "conclusion": "Revisar servidor DHCP", "prioridad": 4},
    {"conditions": ["conexion_inestable", "switch_falla"], "conclusion": "Reiniciar switch o router", "prioridad": 4},
    {"conditions": ["no_imprime", "impresora_apagada"], "conclusion": "Encender impresora", "prioridad": 1},
    {"conditions": ["no_imprime", "impresora_encendida", "ip_incorrecta"], "conclusion": "Asignar IP correcta a impresora", "prioridad": 2},
    {"conditions": ["ping_impresora_falla", "impresora_encendida"], "conclusion": "Revisar conexión de red de la impresora", "prioridad": 2},
    {"conditions": ["sin_conexion_total"], "conclusion": "Revisar conexión WAN o cableado troncal", "prioridad": 5}
]

def diagnosticar(sintomas_usuario):
    diagnosticos = []
    reglas_activadas = []
    coincidencias_parciales = []

    for regla in rules:
        condiciones = regla["conditions"]
        if all(cond in sintomas_usuario for cond in condiciones):
            reglas_activadas.append(regla)
        else:
            coincidencias = [cond for cond in condiciones if cond in sintomas_usuario]
            if coincidencias:
                nivel = len(coincidencias) / len(condiciones)
                coincidencias_parciales.append({
                    "regla": regla,
                    "coinciden": coincidencias,
                    "nivel": nivel
                })

    # Ordenar por prioridad descendente
    reglas_activadas.sort(key=lambda r: r["prioridad"], reverse=True)
    coincidencias_parciales.sort(key=lambda x: (x["nivel"], x["regla"]["prioridad"]), reverse=True)

    # Diagnósticos = solo conclusiones, ordenadas
    diagnosticos = [r["conclusion"] for r in reglas_activadas]

    return diagnosticos, reglas_activadas, coincidencias_parciales

# === Casos de prueba extendidos ===
casos_de_prueba = {
    "Caso 1": ["no_conexion", "router_apagado"],
    "Caso 2": ["no_conexion", "router_encendido", "ping_falla"],
    "Caso 3": ["navegacion_lenta", "muchos_dispositivos"],
    "Caso 4": ["wifi_debil"],
    "Caso 5": ["no_imprime", "impresora_encendida", "ip_incorrecta"],
    "Caso 6": ["no_conexion", "router_encendido"],
}

# === Ejecución de diagnóstico para cada caso ===
for nombre, sintomas in casos_de_prueba.items():
    print(f"\n🔎 {nombre}")
    print(f"Síntomas ingresados: {sintomas}")

    diagnostico, reglas, parciales = diagnosticar(sintomas)

    if diagnostico:
        print("✅ Diagnóstico(s):")
        for r in reglas:
            print(f" - {r['conclusion']} (Prioridad: {r['prioridad']})")
            print(f"   SI {' Y '.join(r['conditions'])} ENTONCES {r['conclusion']}")
    else:
        print("⚠️ No se encontró un diagnóstico exacto.")

    if parciales:
        print("\n🔍 Sugerencias por coincidencia parcial:")
        for p in parciales[:3]:
            porcentaje = int(p["nivel"] * 100)
            prioridad = p["regla"]["prioridad"]
            print(f" - Posible: {p['regla']['conclusion']} ({porcentaje}% coincidencia, prioridad {prioridad})")