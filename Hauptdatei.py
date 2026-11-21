import pandapower as pp



def initialisieren():
    netzwerktemp = pp.create_empty_network('mainnetzwerk', 50)

    # Bus 1, 2 und 3 erstellen mit Knoten Umspannwerk als Slack-Knoten
    b1 = pp.create_bus(netzwerktemp, 110, 'bus_Umspannwerk')
    b2 = pp.create_bus(netzwerktemp, 110, 'bus_Windextgrid')
    b3 = pp.create_bus(netzwerktemp, 110, 'bus_Stadtlast')

    # slack Knoten, sowie Last und Scheinleistungsgenerator anlegen
    pp.create_ext_grid(netzwerktemp, b1, 1.0, 0)
    pp.create_sgen(netzwerktemp, b2, 80, 0)
    pp.create_load(netzwerktemp, b3, 60, 15)

    # Kabel definieren, dazu Datenblatt aus dem Internet besorgen
    kabel1 = pp.create_line_from_parameters(
        netzwerktemp,
        from_bus=b1,
        to_bus=b2,
        length_km=15.0,
        r_ohm_per_km=0.0408,
        x_ohm_per_km=0.115,
        c_nf_per_km=230.0,
        max_i_ka=1.020,  # Die Variable gibt den maximal zulässigen Dauerbetriebsstrom an
        type="cs",  #gibt an ob das Kabel unterirdisch (cs) oder eine Freileitung ist (ol)
        name="A2XS(FL)2Y_64/110kV"
    )

    kabel2 = pp.create_line_from_parameters(
        netzwerktemp,
        from_bus=b2,
        to_bus=b3,
        length_km=15.0,
        r_ohm_per_km=0.0408,
        x_ohm_per_km=0.115,
        c_nf_per_km=230.0,
        max_i_ka=1.020,  # Die Variable gibt den maximal zulässigen Dauerbetriebsstrom an
        type="cs",  #gibt an ob das Kabel unterirdisch (cs) oder eine Freileitung ist (ol)
        name="A2XS(FL)2Y_64/110kV"
    )



    return netzwerktemp

def lastfluss(netz):
    pp.runpp(netz)
    print(netz.res_bus.vm_pu)


def main():
    netzwerk = initialisieren()
    lastfluss(netzwerk)


main()
