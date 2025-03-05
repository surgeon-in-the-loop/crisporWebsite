import pytest
from crispor.guides import find_candidate_guides, design_all_pegRNAs

def test_find_candidate_guides():
    test_seq = "ATG" + "ACGT" * 100 + "TAA"
    guides = find_candidate_guides(test_seq)
    assert len(guides) > 0, "No guides were generated."

def test_design_all_pegRNAs():
    test_seq = "ATG" + "ACGT" * 100 + "TAA"
    mutation_details = {"type": "deletion", "deleted_sequence": "GAG", "position": 1234, "correct_nucleotide": "C"}
    pegRNAs = design_all_pegRNAs(test_seq, mutation_details, 13, 16)
    assert any("forward" in peg for peg in pegRNAs), "No forward pegRNAs generated."
    assert any("reverse" in peg for peg in pegRNAs), "No reverse pegRNAs generated."

