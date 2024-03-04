import fitz
import spacy

# nlp = spacy.load("en_core_web_trf")
# spacy.load("en_core_web_lg")
nlp =  spacy.load("AI_fine_tuning/model-best")
pdfIn = fitz.open("PDF/Medical_Report.pdf")
mask = False



for page in pdfIn:
    text = page.get_text() 
    doc = nlp(text)
    
    
    entities = {ent.text: ent.label_ for ent in doc.ents}
    # print(entities.values())
    text_instances = [page.search_for(text) for text in entities] 
    # print(text_instances)
    # iterate through each instance for highlighting
    for inst, ent in zip(text_instances, entities):
        annot = page.add_highlight_annot(inst)
        
        if mask == True:
            annot.set_colors({"stroke":(0, 0, 0)})
        
        
        else:
            ## Adding comment to the highlighted text
            # print(ent, " : ", entities[ent])
            info = annot.info

            if entities[ent] == "PERSON":
                info["title"] = "Article 4/5/89"
                info["content"] = """Based on Article 4(1) of the GDPR, this information contains data that can be related to an identified or identifiable natural person, in this case, directly by reference to a name. The name and surname of an individual are th­e most common identifiers.

The masking of personal data also complies with Article 5(1)(c) (data minimization) which ensures that information is restricted to what is necessary for the intended processing purposes. 

Article 5(1)(e) emphasizes the principle of storage limitation, specifying that personal data should only be retained in a form that permits identification for as long as necessary; However, personal data processed solely for statistical purposes may be retained for extended periods.

The anonymization process aligns with the principle of storage limitation and complies with the safeguards and measures outlined in Article 89(1)."""
                annot.set_info(info)
            
            elif entities[ent] == "GPE":
                info["title"] = "Article 4/5/89"
                info["content"] = """The address of the hospital is an identifier that, when combined with other pieces of information, can be associated with a person. Based on Article 4(1) of the GDPR, this information qualifies as personal data. 
­
The masking of personal data also complies with Article 5(1)(c) (data minimization) which ensures that information is restricted to what is necessary for the intended processing purposes. 

Article 5(1)(e) emphasizes the principle of storage limitation, specifying that personal data should only be retained in a form that permits identification for as long as necessary; However, personal data processed solely for statistical purposes may be retained for extended periods.

The anonymization process aligns with the principle of storage limitation and complies with the safeguards and measures outlined in Article 89(1)."""
                annot.set_info(info)
            
            elif entities[ent] == "DATE":
                info["title"] = "Article 4/5/89"
                info["content"] = """The date of birth of a person and the date of a medical consultation contains data that can be related to an identified or identifiable natural person. Based on Article 4(1) of the GDPR this information contains personal data.

The masking of personal data also complies with Article 5(1)(c) (data minimization) which ensures that information is restricted to what is necessary for the intended processing purposes. 

Article 5(1)(e) emphasizes the principle of storage limitation, specifying that personal data should only be retained in a form that permits identification for as long as necessary; However, personal data processed solely for statistical purposes may be retained for extended periods.

The anonymization process aligns with the principle of storage limitation and complies with the safeguards and measures outlined in Article 89(1)."""
                annot.set_info(info)
            
            elif entities[ent] == "ID":
                info["title"] = "Article 4/5/89"
                info["content"] = """The ID in medical reports directly identifies individuals, serving as a unique patient identifier within the healthcare system. As per Article 4(1) of the GDPR, this qualifies as personal data.

The masking of personal data also complies with Article 5(1)(c) (data minimization) which ensures that information is restricted to what is necessary for the intended processing purposes. 

Article 5(1)(e) emphasizes the principle of storage limitation, specifying that personal data should only be retained in a form that permits identification for as long as necessary; However, personal data processed solely for statistical purposes may be retained for extended periods.

The anonymization process aligns with the principle of storage limitation and complies with the safeguards and measures outlined in Article 89(1)."""
                annot.set_info(info)
            
            elif entities[ent] == "INSURANCE":
                info["title"] = "Article 4/5/89"
                info["content"] = """An individual's insurance number is considered personal data due to its direct association with their financial and health-related information, uniquely identifying them. In accordance with Article 4(1) of the GDPR, this information contains personal data.

The masking of personal data also complies with Article 5(1)(c) (data minimization) which ensures that information is restricted to what is necessary for the intended processing purposes. 

Article 5(1)(e) emphasizes the principle of storage limitation, specifying that personal data should only be retained in a form that permits identification for as long as necessary; However, personal data processed solely for statistical purposes may be retained for extended periods.

The anonymization process aligns with the principle of storage limitation and complies with the safeguards and measures outlined in Article 89(1)."""
                annot.set_info(info)
            
            elif entities[ent] == "EMAIL":
                info["title"] = "Article 4/5/89"
                info["content"] = """An email address contains information that directly relates to an individual. Based on Article 4(1) of the GDPR, an email address is considered personal data.
The masking of personal data also complies with Article 5(1)(c) (data minimization) which ensures that information is restricted to what is necessary for the intended processing purposes. 

Article 5(1)(e) emphasizes the principle of storage limitation, specifying that personal data should only be retained in a form that permits identification for as long as necessary; However, personal data processed solely for statistical purposes may be retained for extended periods.

The anonymization process aligns with the principle of storage limitation and complies with the safeguards and measures outlined in Article 89(1)."""
                annot.set_info(info)
            
            elif entities[ent] == "CREDIT_CARD":
                info["title"] = "Article 4/5/89"
                info["content"] = """A credit card serves as an identifier reflecting the financial identity of an individual, directly or indirectly associated with them. According to Article 4(1) of the GDPR, this information constitutes personal data.

The masking of personal data also complies with Article 5(1)(c) (data minimization) which ensures that information is restricted to what is necessary for the intended processing purposes. 

Article 5(1)(e) emphasizes the principle of storage limitation, specifying that personal data should only be retained in a form that permits identification for as long as necessary; However, personal data processed solely for statistical purposes may be retained for extended periods.

The anonymization process aligns with the principle of storage limitation and complies with the safeguards and measures outlined in Article 89(1)."""
                annot.set_info(info)
            else:
                print("Unknown entity value")


            
        annot.update()



# Saving the PDF Output
pdfIn.save("Medical_Report_masked.pdf")

