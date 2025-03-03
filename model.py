import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Subir la imagen
path = "perro.jpg"

image = Image.open(path)

def predict_image(image):
    np.set_printoptions(suppress=True)

    model = tf.keras.models.load_model("/content/modelo_razas_perros.h5", compile=False)

    class_names = ['affenpinscher', 'african', 'airedale', 'akita', 'appenzeller', 'australian_kelpie',
                   'australian_shepherd', 'bakharwal_indian', 'basenji', 'beagle', 'bluetick', 'borzoi',
                   'bouvier', 'boxer', 'brabancon', 'briard', 'buhund_norwegian', 'bulldog_boston',
                   'bulldog_english', 'bulldog_french', 'bullterrier_staffordshire', 'cattledog_australian',
                   'cavapoo', 'chihuahua', 'chippiparai_indian', 'chow', 'clumber', 'cockapoo', 'collie_border',
                   'coonhound', 'corgi_cardigan', 'cotondetulear', 'dachshund', 'dalmatian', 'dane_great',
                   'danish_swedish', 'deerhound_scottish', 'dhole', 'dingo', 'doberman', 'elkhound_norwegian',
                   'entlebucher', 'eskimo', 'finnish_lapphund', 'frise_bichon', 'gaddi_indian', 'germanshepherd',
                   'greyhound_italian', 'groenendael', 'havanese', 'hound_afghan', 'hound_basset', 'hound_blood',
                   'hound_english', 'hound_ibizan', 'hound_plott', 'hound_walker', 'husky', 'keeshond', 'kelpie',
                   'kombai', 'komondor', 'kuvasz', 'labradoodle', 'labrador', 'leonberg', 'lhasa', 'malamute',
                   'malinois', 'maltese', 'mastiff_bull', 'mastiff_english', 'mastiff_indian', 'mastiff_tibetan',
                   'mexicanhairless', 'mountain_bernese', 'mountain_swiss', 'newfoundland', 'otterhound',
                   'ovcharka_caucasian', 'papillon', 'pariah_indian', 'pekinese', 'pembroke', 'pinscher_miniature',
                   'pitbull', 'pointer_german', 'pomeranian', 'poodle_miniature', 'poodle_standard', 'poodle_toy',
                   'pug', 'puggle', 'pyrenees', 'rajapalayam_indian', 'redbone', 'retriever_chesapeake',
                   'retriever_curly', 'retriever_flatcoated', 'retriever_golden', 'ridgeback_rhodesian',
                   'rottweiler', 'saluki', 'samoyed', 'schipperke', 'schnauzer_giant', 'schnauzer_miniature',
                   'segugio_italian', 'setter_english', 'setter_gordon', 'setter_irish', 'sharpei', 'sheepdog_english',
                   'sheepdog_shetland', 'shiba', 'shihtzu', 'spaniel_blenheim', 'spaniel_brittany', 'spaniel_cocker',
                   'spaniel_irish', 'spaniel_japanese', 'spaniel_sussex', 'spaniel_welsh', 'spitz_indian',
                   'spitz_japanese', 'springer_english', 'stbernard', 'terrier_american', 'terrier_australian',
                   'terrier_bedlington', 'terrier_border', 'terrier_cairn', 'terrier_dandie', 'terrier_fox',
                   'terrier_irish', 'terrier_kerryblue', 'terrier_lakeland', 'terrier_norfolk', 'terrier_norwich',
                   'terrier_patterdale', 'terrier_russell', 'terrier_scottish', 'terrier_sealyham', 'terrier_silky',
                   'terrier_tibetan', 'terrier_toy', 'terrier_westhighland', 'terrier_wheaten', 'terrier_yorkshire',
                   'tervuren', 'vizsla', 'waterdog_spanish', 'weimaraner', 'whippet', 'wolfhound_irish']

    image = image.convert("RGB")
    size = (150, 150)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data = np.ndarray(shape=(1, 150, 150, 3), dtype=np.float32)
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return"Tu perro es un ", confidence_score,"% ", class_name[2:], "."

predict_image(image)
