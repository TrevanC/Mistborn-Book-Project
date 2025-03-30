import pandas as pd
import numpy as np
import spacy
from spacy import displacy
import networkx as nx

import matplotlib.pyplot as plt
from collections import Counter

import pyvis
from pyvis.network import Network
import community as community_louvain

def character_df_init(character_filename):
    character_df = pd.read_csv(character_filename, header=None, names=["character"])
    character_df['character_firstname'] = character_df['character'].str.split().str[0]
    return character_df


def ner_and_patterns_init(character_df):
    """reads in list of characters, activates nsr, then create
    
    """
    ner = spacy.load("en_core_web_sm")
    ruler = ner.add_pipe("entity_ruler", before="ner")
    
    #Define character names as patterns for spacy

    names = character_df['character'].tolist()
    first = character_df['character_firstname'].tolist()
    
    first_name_counter = Counter(first)
    dup_first_name = [x[0] for x in first_name_counter.items() if x[1] > 1]
    
    names = names + first
    names = list(set(names))
    names = sorted(names)
    block_list = set(dup_first_name)
    names = [x for x in names if x not in block_list]
     
    patterns = [{"label": "PERSON", "pattern": name} for name in names]
    
    ruler.add_patterns(patterns)
    return ner

def book_init(ner, book_filename):
    book_text = open(book_filename).read()
    book_doc = ner(book_text)
    
    return book_doc

def get_entity_list_per_sentence(spacy_doc):
    """
    """
    sent_entity_df = []
        
    #loop through sentences, store named entity list for each sentence
    for sent in spacy_doc.sents:
        entity_list = [ent.text for ent in sent.ents]
        sent_entity_df.append({"sentence": sent, "entities": entity_list})
    
    return sent_entity_df

                               
def filter_entity(ent_list, character_df):
    """
    function filters out non-character entities
    """
    return [ent for ent in ent_list
        if ent in list(character_df.character)
        or ent in list(character_df.character_firstname)]


def create_relationships(df, window_size):
    """
    """    
    relationships = []

    for i in range(df.index[-1]):
        end_i = min(i+5, df.index[-1])
        char_list = sum((df.loc[i: end_i].character_entities), [])
        #remove duplicated characters within window
        char_unique = [char_list[i] for i in range(len(char_list))
                       if (i==0) or char_list[i] != char_list[i-1]]
        if len(char_unique) > 1:
            for idct, a in enumerate(char_unique[:-1]):
                b = char_unique[idct + 1]
                relationships.append({"source": a, "target": b})
            
    relationship_df = pd.DataFrame(relationships)
    
    #reverse order in case of reverse duplicate relations
    relationship_df = pd.DataFrame(np.sort(relationship_df.values, axis = 1), columns = relationship_df.columns)
    
    #Aggregate rows + create a weight column
    relationship_df["value"] = 1
    relationship_df = relationship_df.groupby(["source", "target"], sort=False, as_index=False).sum()
    
    return relationship_df