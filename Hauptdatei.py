import pandapower as pp
import numpy as np




def initialisieren():
    netzwerktemp = pp.create_empty_network('mainnetzwerk', 50)

    # Bus 1, 2 und 3 erstellen mit Knoten Umspannwerk als Slack-Knoten
    b1 = pp.create_bus(netzwerktemp, 110, 'bus_Umspannwerk', geodata= (0, 0))
    b2 = pp.create_bus(netzwerktemp, 110, 'bus_Windextgrid', geodata=(10, 0))
    b3 = pp.create_bus(netzwerktemp, 110, 'bus_Stadtlast' , geodata=(20, 0))

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
    #Spannung an den Busschienen
    print(netz.res_bus.vm_pu)
    print()
    print(netz.res_line.loading_percent)
    print()
    print(netz.res_line.pl_mw)

def netzplot(netz):
    #ausgelagert, falls Bedarf an weiteren Parametern besteht
    pp.plotting.simple_plot(
        netz,
        respect_switches=False,
        line_width=15,         # Kabeldicke
        bus_size=8,          # Bus-Kreise deutlich größer als die Kabel
        ext_grid_size=8,     # Quadrat des Slack-Netzes groß darstellen
        plot_loads=True,        # Last-Dreieck aktivieren
        load_size=8,         # Größe des Last-Dreiecks
        plot_sgens=True,        # Erzeuger-Symbol (Windpark) aktivieren
        sgen_size=8,   # Größe des Erzeuger-Symbols
        bus_color="darkblue",
        line_color="grey",
        show_plot=True,

    )

def main():
    netzwerk = initialisieren()
    lastfluss(netzwerk)
    netzplot(netzwerk)


main()
