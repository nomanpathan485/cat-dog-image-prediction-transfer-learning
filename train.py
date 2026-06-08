import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import(
    Dense,
    GlobalAveragePooling2D
)
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

train_dataset = tf.keras.utils.image_dataset_from_directory(
    "cat-dog-image-classifier-cnn/dataset/PetImages",
    validation_split = 0.2,
    subset = "training",
    seed = 42,
    image_size=(128,128),
    batch_size=32
)

val_dataset = tf.keras.utils.image_dataset_from_directory(
    "cat-dog-image-classifier-cnn/dataset/PetImages",
    validation_split =0.2,
    subset = "validation",
    seed =42,
    image_size=(128,128),
    batch_size=32
)
train_dataset = train_dataset.map(
    lambda x, y: (preprocess_input(x), y)
)

val_dataset = val_dataset.map(
    lambda x, y: (preprocess_input(x), y)
)

base_model = MobileNetV2(
    weights = "imagenet",
    include_top=False,
    input_shape = (128,128,3)
)
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128,activation="relu"),
    Dense(1, activation="sigmoid")
])
model.summary()

model.compile(
    optimizer=Adam(learning_rate=0.00001),
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)
history = model.fit(
    train_dataset,
    validation_data = val_dataset,
    epochs = 3
)
model.save("cat_dog_transfer_model.keras")