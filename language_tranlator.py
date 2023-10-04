import goslate 
inserted_text = "This is an English Language"
gs= goslate.Goslate()

# first argu is the input text, second argu is to which lang want to translate
#   Here, 'fr' stands for french
translated_text = gs.translate(inserted_text, 'fr')

print(translated_text)