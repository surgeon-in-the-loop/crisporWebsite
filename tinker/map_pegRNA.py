import json
from crispor.guides import design_all_pegRNAs
from crispor.utils import fetch_gene_sequence

def main():
    with open('tor1a_config.json', 'r') as f:
        config = json.load(f)
    
    target_seq = fetch_gene_sequence(config["gene"])
    
    pegRNAs = design_all_pegRNAs(
        target_seq, 
        config["mutation"], 
        config["prime_editing"]["pbs_length"], 
        config["prime_editing"]["rtt_length"]
    )
    
    for peg in pegRNAs:
        print("Candidate pegRNA:", peg)

if __name__ == "__main__":
    main()

