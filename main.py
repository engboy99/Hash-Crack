import argparse
from hash_crack.core import hash_string
from hash_crack.detect import detect_hash_type
from hash_crack.local_cracker import crack_hash_locally
from hash_crack.api_clients import crack_hash_online
from hash_crack.ai_cracker import ai_predict_hash
from hash_crack.async_cracker import async_crack

def main():
    parser = argparse.ArgumentParser(description='Hash-Buster: Advanced Hash Cracker')
    parser.add_argument('-t', '--type', help='Detect hash type', action='store_true')
    parser.add_argument('-c', '--crack', help='Crack the given hash')
    parser.add_argument('-a', '--ai', help='AI-based hash prediction', action='store_true')
    parser.add_argument('-m', '--method', choices=['local', 'online', 'async'], default='local', help='Choose cracking method')
    
    args = parser.parse_args()
    
    if args.type:
        hash_type = detect_hash_type(args.crack)
        print(f'Detected Hash Type: {hash_type}')
    
    if args.crack:
        if args.method == 'local':
            result = crack_hash_locally(args.crack)
        elif args.method == 'online':
            result = crack_hash_online(args.crack)
        elif args.method == 'async':
            result = async_crack(args.crack)
        
        print(f'Crack Result: {result}')
    
    if args.ai:
        ai_result = ai_predict_hash(args.crack)
        print(f'AI Prediction: {ai_result}')
    
if __name__ == '__main__':
    main()
