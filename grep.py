import re, sys, os
from colorama import init, Fore


init(convert=True)

def grep(pattern, filename):
    try:
        found_match = False
        with open(filename, 'r') as file:
            print(Fore.BLUE + 'Searching ' + filename.split('\'')[-1] + Fore.RESET + '\n')
            for line in file:
                match = re.search(pattern, line)
                if match:
                    print(Fore.GREEN + line.strip() + "\n")
                    found_match = True
        if not found_match:
            print(Fore.RED + f"No content found matching the pattern '{pattern}'.")
    except FileNotFoundError:
        print(Fore.RED + f"File '{filename}' not found.")
   
   

if len(sys.argv) < 5:
    print(Fore.RED + "Usage: python grep_python.py -p <pattern> -e <filename> <-fn>\n  -fn  -for searching in file names")
    sys.exit(1)
    
for i in range(len(sys.argv)):
    if '-' in sys.argv[i]:
        sys.argv[i] = sys.argv[i].lower()
        

pattern = sys.argv[sys.argv.index('-p')+1] or None
filename = sys.argv[sys.argv.index('-e')+1] or None


if pattern is None or filename is None:
    print(Fore.RED + "Usage: python grep_python.py -p <pattern> -e <filename> <-fn>\n  -fn  -for searching in file names")
    sys.exit(1)


if '.' in filename and not '-fn' in sys.argv:
    grep(pattern, filename)
elif '.' in filename and '-fn' in sys.argv and len(filename) > 1:
    print(Fore.RED + "Usage: python grep_python.py -p <pattern> -e <filename> <-fn>\n  -fn  -for searching in file names")
    sys.exit(1)
else:
    if os.path.exists(filename):
        if '-fn' in sys.argv:
            founded = False
            for i in os.listdir(os.path.join(os.getcwd(), filename)):
                match = re.search(pattern, i)
                if match:
                    founded = True
                    print(Fore.GREEN + i.strip())
            if not founded:
                print(Fore.RED + f"Pattern '{pattern}' not found in directory."+ Fore.RESET)
        else:        
            for i in os.listdir(os.path.join(os.getcwd(),filename)):
                grep(pattern=pattern, filename=os.path.join(os.getcwd(),filename,i))
    else:
        if '-fn' in sys.argv:
            print(Fore.RED + f"Directory '{filename}' not found.")
            exit(1)
        founded = False
        for i in filename.split():
            match = re.search(pattern, i)
            if match:
                founded = True
                print(Fore.GREEN + i.strip())
        if not founded:
            print(Fore.RED + f"Pattern '{pattern}' not found in text."+ Fore.RESET)
            
        