from utils.parameters import Parameters
from lib.parser import make_uri, addr_parser

if __name__=='__main__':

    sleep_secs = 0
    city_area = Parameters.CITY_AREA

    uri = make_uri(city_area)
    addr_parser(uri, sleep_secs)