import os
import sys
import Cards as car

#decay channels

def decay_x2():
    decay_prod = raw_input('Type the decay channel:\n'\
                           "(possible SM decay products (don't include x1): u, d, c, s, b, t, e, mu, ta, j, a)\n")
    return decay_prod

def decay_s2():
    decay_prod = raw_input('Type the decay channel:\n'\
                           "(possible SM decay products: u, d, c, s, b, t, e, mu, ta, j, a)\n")
    return decay_prod

#different topologies

def LLP_MET():
    #initial and decaying states
    in_state = raw_input('Type the initial state: \n')
    dec_state = raw_input('Type the decaying state: \n'\
                          '(either s2~ s1 or s2 s1~, x2~ x1 or x2 x1~)\n')
    if (dec_state == 'x1 x2~' or dec_state == 'x2~ x1' or dec_state == 'x1~ x2' or dec_state == 'x2 x1~'):
        if 'x2' in dec_state:
            dec_state = 'x2 x1~'
        elif 'x2~' in dec_state:
            dec_state = 'x2~ x1'
        decay_prod = decay_x2()
        process = in_state + ' > zp > ' + dec_state + ' / x2 s2 j, (x2 > x1 ' + decay_prod + ' /zp), (x2~ > x1~ ' + decay_prod + ' / zp)'
    elif (dec_state == 's1~ s2' or dec_state == 's2~ s1' or dec_state == 's1 s2~' or dec_state == 's2 s1~'):
        if 's2' in dec_state:
            dec_state = 's2 s1~'
        elif 's2~' in dec_state:
            dec_state = 's2~ s1'
        decay_prod = decay_s2()
        process = in_state + ' > zp > ' + dec_state + ' / x2 s2 j, (s2 > ' + decay_prod + ' /zp), (s2~ > ' + decay_prod + ' /zp)'
    else:
        print 'ERROR: the process is not valid.'
        sys.exit()
    print 'The process is ' + process
    return process, decay_prod

def double_LLP():
    #initial and decaying states
    in_state = raw_input('Type the initial state: \n')
    dec_state = raw_input('Type the decaying state: \n'\
    '(either s2 s2~ or x2 x2~)\n')
    if (dec_state == 'x2 x2~' or dec_state == 'x2~ x2'):
        dec_state = 'x2 x2~'
        decay_prod = decay_x2()
        process = in_state + ' > ' + dec_state + ' / x2 s2 j, (x2 > x1 ' + decay_prod + ' / zp), (x2~ > x1~ ' + decay_prod + ' / zp)'
    elif dec_state == 's2 s2~' or dec_state == 's2~ s2':
        dec_state = 's2 s2~'
        decay_prod = decay_s2()
        process = in_state + ' > ' + dec_state + ' / x2 s2 j, (s2 > ' + decay_prod + ' / zp), (s2~ > ' + decay_prod + ' /zp)'
    else:
        print 'ERROR: the process is not valid.'
        sys.exit()
    print 'The process is ' + process
    return process, decay_prod

def double_LLP_MET():
    #initial and decaying states
    in_state = raw_input('Type the initial state: \n')
    dec_state = raw_input('Type the decaying state: \n'\
                          '(either x2 x2~ s1 s1~ or s2 s2~ x1 x1~)\n')
    if (dec_state == 'x2 x2~ s1~ s1' or dec_state == 'x2~ x2 s1~ s1' or
        dec_state == 's1~ s1 x2~ x2' or dec_state == 's1~ s1 x2 x2~' or
        dec_state == 'x2 s1~ x2~ s1' or dec_state == 'x2~ s1~ x2 s1' or
        dec_state == 'x2 x2~ s1 s1~' or dec_state == 'x2~ x2 s1 s1~' or
        dec_state == 's1 s1~ x2~ x2' or dec_state == 's1 s1~ x2 x2~' or
        dec_state == 'x2 s1 x2~ s1~' or dec_state == 'x2~ s1 x2 s1~'):
        dec_state = 'x2 x2~ s1 s1~'
        decay_prod = decay_x2()
        process = in_state + ' > ' + dec_state + ' / x2 s2 j, (x2 > x1 ' + decay_prod + ' / zp), (x2~ > x1~ ' + decay_prod + ' / zp)'
    elif (dec_state == 'x1 x1~ s2~ s2' or dec_state == 'x1~ x1 s2~ s2' or
        dec_state == 's2~ s2 x1~ x1' or dec_state == 's2~ s2 x1 x1~' or
        dec_state == 'x1 s2~ x1~ s2' or dec_state == 'x1~ s2~ x1 s2' or
        dec_state == 'x1 x1~ s2 s2~' or dec_state == 'x1~ x1 s2 s2~' or
        dec_state == 's2 s2~ x1~ x1' or dec_state == 's2 s2~ x1 x1~' or
        dec_state == 'x1 s2 x1~ s2~' or dec_state == 'x1~ s2 x1 s2~'):
        dec_state = 's2 s2~ x1 x1~'
        decay_prod = decay_s2()
        process = in_state + ' > ' + dec_state + ' / x2 s2 j, (s2 > ' + decay_prod + ' / zp), (s2~ > ' + decay_prod + ' /zp)'
    else:
         print 'ERROR: the process is not valid.'
         sys.exit()
    print 'The process is ' + process
    return process, decay_prod
                           

#execution

def execute(proc_card,out_name,madspin_card):
    check = not os.path.isdir('./LLP_cards')
    if check == True:
        os.mkdir('./LLP_cards')
    os.system('mv ' + proc_card + ' ./LLP_cards/')
    os.system('mv param_card.dat ./LLP_cards/')
    os.system('mv ' + madspin_card + ' ./LLP_cards/')
    choice = raw_input('Do you want to create the folder of the process? \n')
    if (choice == 'y') or (choice == 'yes'):
        os.system('./bin/mg5_aMC ./LLP_cards/' + proc_card)
        os.system('cp ./LLP_cards/param_card.dat proc_' + out_name + '/Cards/')
        os.system('cp ./LLP_cards/' + madspin_card + ' proc_' + out_name + '/Cards/')
        print 'The madspin and parameter cards have already been copied into ./proc_' + out_name + '/Cards/'
    os.remove('Cards.pyc')


def main():
    topology = ['1: LLP + MET','2: 2xLLP','3: 2xLLP + MET']
    choice = raw_input('Type the topology you are interested in: \n'\
                       '' + topology[0] + '\n'\
                       '' + topology[1] + '\n'\
                       '' + topology[2] + '\n')

    if choice == '1' or choice == '2' or choice == '3':
        
        #choice of topology
        
        #LLP + MET
        if choice == '1':
            print 'You chose topology: ' + choice + ' - ' + topology[int(choice)-1].split()[1] + ' ' + topology[int(choice)-1].split()[2] + ' ' + topology[int(choice)-1].split()[3]
            
            process, decay = LLP_MET()
            
            car.param_card(process,choice)
            proc_card, out_name = car.proc_card(process,choice)
            madspin_card = car.madspin_card(process,decay)
            
            #execution
            execute(proc_card,out_name,madspin_card)

        # 2xLLP
        if choice == '2':
            print 'You chose topology: ' + choice + ' - ' + topology[int(choice)-1].split()[1]
        
            process, decay = double_LLP()

            car.param_card(process,choice)
            proc_card, out_name = car.proc_card(process,choice)
            madspin_card = car.madspin_card(process,decay)
            
            #execution
            execute(proc_card,out_name,madspin_card)

        #2xLLP + MET
        if choice == '3':
            print 'You chose topology: ' + choice + ' - ' + topology[int(choice)-1].split()[1] + ' ' + topology[int(choice)-1].split()[2] + ' ' + topology[int(choice)-1].split()[3]
        
            process, decay = double_LLP_MET()

            car.param_card(process,choice)
            proc_card, out_name = car.proc_card(process,choice)
            madspin_card = car.madspin_card(process,decay)
            
            #execution
            execute(proc_card,out_name,madspin_card)

    else:
            print "ERROR: You didn't choose one of the default possibilities."

main()

