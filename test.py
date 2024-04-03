from qdrant_client import QdrantClient

import json

# Initialize the client
client = QdrantClient(host="localhost", port=6333)  # or QdrantClient(path="path/to/db")

with open("output copy.json","r",encoding="utf-8") as docs:
    content = json.load(docs)
    
docs2 = []
for x in content:
    text = "question: "+ x["question"] + " reponse: "+ x["reponse"] +" source: "+ x["source"] + " date: "+ x["date"]
    docs2.append(text)

# Prepare your documents, metadata, and IDs
docs1 =[ "question:  Qu'est-ce qu'Orange Côte d'Ivoire ?   reponse:  Orange Côte d'Ivoire (Orange CI ou OCI) est un opérateur de télécommunications leader en Côte d'Ivoire. Ils proposent une large gamme de services, y compris la téléphonie fixe et mobile, l'internet (3G, 4G, fibre), le Mobile Banking et la télévision.   source:    date :  2024-03-19",
        "question:  Quelle est le nombre d'abonnées sur linkedin d'Orange Côte d'Ivoire ?   reponse:  Orange CI compte 152 K abonnés sur linkedin   source:    date :  2024-03-19",
        "question:  Quand Orange Côte d'Ivoire a-t-elle été créée ?   reponse:  Orange CI a été créée en 1996.   source:    date :  2024-03-19",
        "question:  Quels sont les services offerts par Orange Côte d'Ivoire ?   reponse:  Orange CI offre une gamme complète de services de télécommunications, notamment :Téléphonie fixe et mobile,Internet (3G, 4G, fibre),Mobile Banking,Télévision,Services digitaux   source:    date :  2024-03-19",
        "question:  Qu'est-ce qui distingue Orange Côte d'Ivoire de ses concurrents ?   reponse:  Orange CI se distingue par son engagement envers l'innovation, la qualité et la responsabilité sociétale d'entreprise. Ils ont été certifiés ISO 9001 et Top Employer, et ils ont réalisé plus de 390 projets sociaux à travers la Fondation Orange Côte d'Ivoire.   source:    date :  2024-03-19",
        "question:  Où puis-je trouver plus d'informations sur Orange Côte d'Ivoire ?   reponse:  Vous pouvez trouver plus d'informations sur Orange Côte d'Ivoire sur leur site web : http://www.orangebusiness.ci   source:    date :  2024-03-19",
        "question:  Quelles sont les initiatives RSE d'Orange Côte d'Ivoire ?   reponse:  Orange CI s'engage dans plusieurs initiatives RSE, notamment dans les domaines de la santé, de l'éducation et de la culture. Ils ont réalisé plus de 390 projets sociaux à travers la Fondation Orange Côte d'Ivoire.   source:    date :  2024-03-19",
        "question:  Quelles sont les conditions de travail chez Orange Côte d'Ivoire ?   reponse:  : Orange CI offre des conditions de travail et de santé exceptionnelles à ses employés. Ils ont été certifiés Top Employer quatre années consécutives (2014-2017).   source:    date :  2024-03-19",
        "question:  Quelles sont les perspectives d'avenir pour Orange Côte d'Ivoire ?   reponse:  Orange CI continue d'investir dans l'innovation et le développement de ses réseaux. Ils visent à devenir le leader de la transformation digitale en Côte d'Ivoire.   source:    date :  2024-03-19",
        "question:  Comment puis-je contacter Orange Côte d'Ivoire ?   reponse:  Vous pouvez contacter Orange CI via leur site web, leur page Facebook, ou en appelant leur service client.   source:    date :  2024-03-19",
        "question:  Quelle est la position d'Orange CI sur le marché ivoirien ?   reponse:  Orange CI est le leader de la téléphonie mobile en Côte d'Ivoire avec près de 12 882 895 d'abonnés en Mars 2017 (selon l'ARTCI).   source:    date :  2024-03-19",
        "question:  Quand Orange Côte d'ivoire a fusionné avec Côte d'Ivoire Telecom ?   reponse:  Orange Côte d'ivoire a fusionné le 31 décembre 2016 avec Côte d’Ivoire Telecom   source:    date :  2024-03-19",
        "question:  Quelles sont les filiales d'Orange CI ?   reponse:  Orange CI a racheté Cellcom-Libéria et Airtel-Burkina Faso en 2017, qui sont devenues respectivement Orange Libéria et Orange Burkina Faso.   source:    date :  2024-03-19",
        "question:  Quelles sont les certifications d'Orange CI ?   reponse:  Orange CI est certifiée ISO 9001 par l'AFAQ-AFNOR pour sa démarche Qualité et Top Employer 2014, 2015, 2016 et 2017 pour ses conditions de travail et de santé exceptionnelles.   source:    date :  2024-03-19",
        "question:  Combien d'employés compte Orange CI ?   reponse:  Orange CI compte entre 1 001 et 5 000 employés et 2 115 membres associés.   source:    date :  2024-03-19",
        "question:  Que propose Orange CI en tant qu'entreprise citoyenne ?   reponse:  Orange CI s'engage dans la Responsabilité Sociétale d'Entreprise (RSE) et a réalisé plus de 390 projets sociaux (santé, éducation, culture) à travers la Fondation Orange Côte d'Ivoire.   source:    date :  2024-03-19",
        "question:  Qu'elle est le slogan d'orange   reponse:  Vous rapprocher de l'essentiel   source:    date :  2024-03-19",
        "question:  Quelle est le nombre de followers sur instagram d'Orange Côte d'Ivoire ?   reponse:  Orange CI compte 229 K de followers   source:    date :  2024-03-19",
        "question:  Qui est le Directeur Général du Groupe Orange d'Ivoire ?   reponse:  Mamadou Bamba est le Directeur Général du Groupe Orange d'Ivoire.   source:    date :  2024-03-19",
        "question:  Qui est la Directrice Générale Adjointe du Groupe Orange Côte   reponse:  Nafy Coulibaly Silué est la Directrice Générale Adjointe du Groupe Orange Côte d'Ivoire.   source:    date :  2024-03-19",
        "question:  Qui est le Directeur Général d'Orange Libéria ?   reponse:  Marius Yao est le Directeur Général d'Orange Libéria.   source:    date :  2024-03-19",
        "question:  Qui est le Directeur Général d'Orange Burkina ?   reponse:  Mamadou Coulibaly est le Directeur Général d'Orange Burkina.   source:    date :  2024-03-19",
        "question:  Qui est la Directrice Générale d'Orange Money Côte d'Ivoire ?   reponse:  Mariame Toure est la Directrice Générale d'Orange Money Côte d'Ivoire.   source:    date :  2024-03-19",
        "question:  Qui est le Directeur Général de Côte d'Ivoire Câbles ?   reponse:  Koné Kolo est le Directeur Général de Côte d'Ivoire Câbles.   source:    date :  2024-03-19",
        "question:  Quelle est la mission d'Orange CI en Afrique subsaharienne ?   reponse:  La mission d'Orange CI en Afrique subsaharienne est de connecter les populations et de leur donner accès aux avantages du numérique.   source:  https://groupe.orange.ci/fr/engagement-operateur-engage.html  date :  2024-03-19",
        "question:  Quels sont les engagements d'Orange CI en matière de développement durable ?   reponse:  Orange CI s'engage à rendre le numérique accessible à tous et à contribuer aux Objectifs de Développement Durable (ODD), notamment en matière d'éducation, de santé et d'inclusion sociale.   source:  https://groupe.orange.ci/fr/engagement-operateur-engage.html  date :  2024-03-19",
        "question:  Quels sont les programmes mis en place par Orange CI pour favoriser l'inclusion numérique ?   reponse:  Orange CI a mis en place plusieurs programmes, tels que les Orange Digital Centers, qui visent à former les jeunes aux métiers du numérique, à développer l'entrepreneuriat numérique et à sensibiliser les populations aux usages du numérique.   source:  https://groupe.orange.ci/fr/engagement-operateur-engage.html  date :  2024-03-19",
        "question:  Comment Orange CI accompagne-t-elle la révolution digitale du secteur de la santé ?   reponse:  Orange CI propose des solutions digitales pour améliorer la gestion des patients, la télémédecine et la formation des professionnels de la santé.   source:  https://groupe.orange.ci/fr/engagement-operateur-engage.html  date :  2024-03-19"
    ]
metadata = [
        {"source": "orange-docs"},
        {"source": "orangeci-docs"},
    ]



print("ok miss")
# Use the new add method
client.add(
    collection_name="Corpus V2",
    documents=docs2,
    
    
)

# search_result = client.query(
#     collection_name="gaye",
#     query_text="Comment Orange CI accompagne-t-elle la révolution digitale du secteur de la santé ?"
# )
# print(search_result)
