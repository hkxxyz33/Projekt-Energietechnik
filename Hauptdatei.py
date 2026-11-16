import pandapower as pp
import pandapower.networks as nw
#import

def main():
    netzwerk = pp.create_empty_network('mainnetzwerk', 50)

    #Bus 1, 2 und 3 erstellen mit Knoten Umspannwerk als Slack-Knoten
    pp.create_bus(netzwerk, 110, 'bus_Umspannwerk', 1)
    pp.create_bus(netzwerk, 110, 'bus_Windextgrid', 2)
    pp.create_bus(netzwerk, 110, 'bus_Stadtlast', 3)

    #slack Knoten, sowie Last und Scheinleistungsgenerator anlegen
    pp.create_ext_grid(netzwerk, 1, 1.0, 0)
    pp.create_load(netzwerk, 3, 60000000, 15000000)
    pp.create_sgen(netzwerk, 2, 80000000, 0)

    #Kabel definieren, dazu Datenblatt aus dem Internet besorgen
    leitungskabel = pp.create_line_from_parameters(
        netz,
        bus1,
        bus2,
        länge,
        Widerstandsbelag,
        Blindleistungsbelag,
        kapazitätsbelag,
        max_i_ka bedeutet? maximal thermal current in kA was ist thermal current,


        Induktivitätsbelag???


    )