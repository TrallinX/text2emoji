import sys

AUTOR = 'Sviborg'
DATE = '07/12/2017'

emoji_symbols={'0':':zero:', '1' :':one:', '2': ':two:', '3': ':three:', '4': ':four:', '5': ':five:', '6': ':six:', '7': ':seven:', '8':  ':eight:', '9': ':nine:', 'a' : ':regional_indicator_a:', 'b' : ':regional_indicator_b:', 'c' : ':regional_indicator_c:', 'd' : ':regional_indicator_d:', 'e' : ':regional_indicator_e:', 'f' : ':regional_indicator_f:', 'g' : ':regional_indicator_g:', 'h' : ':regional_indicator_h:', 'i' : ':regional_indicator_i:', 'j' : ':regional_indicator_j:', 'k' : ':regional_indicator_k:', 'l' : ':regional_indicator_l:', 'm' : ':regional_indicator_m:', 'n' : ':regional_indicator_n:', 'o' : ':regional_indicator_o:', 'p' : ':regional_indicator_p:', 'q' : ':regional_indicator_q:', 'r' : ':regional_indicator_r:', 's' : ':regional_indicator_s:', 't' : ":regional_indicator_t:", 'u' : ':regional_indicator_u:', 'v' : ':regional_indicator_v:', 'w' : ':regional_indicator_w:', 'x' : ':regional_indicator_x:', 'y' : ':regional_indicator_y:', 'z' : ':regional_indicator_z:', '-' : ':heavy_minus_sign:', '+' : ':heavy_plus_sign:', '=' : '=', '?' : ':grey_question:', '!' : ' :grey_exclamation:', '.' : '.', ',' : ',' }

try:
    if sys.argv[1] == "-h":
        print('usage: python emoji2text [-h] "<text>"')
    else:
        text = sys.argv[1]
        final_text = ''
        for symbol in text.lower():
            if symbol == ' ':
                final_text = final_text + '  '
            else:
                try:
                    final_text = final_text + ' ' +emoji_symbols[symbol]
                except KeyError:
                    print('error: found not allowed symbol')
                    exit(-1)
        print(final_text)
except IndexError:
    print('usage: python text2emoji "<text>"')
