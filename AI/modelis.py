import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Nolasa iztīrītos datus.
df = pd.read_csv("tirs.csv")

# Atdala prognozējamo kolonnu no pārējiem datiem.
X = df.drop("response_tier", axis=1)
y = df["response_tier"]

# Sadala datus treniņa un testa daļā.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Atrodam kategoriskās kolonnas.
categorical_columns = X.select_dtypes(include=["object"]).columns

# Pārvēršam tekstuālās kolonnas skaitļos.
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)
    ],
    remainder="passthrough"
)

# Izveidojam modeli.
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", DecisionTreeClassifier(random_state=42))
])

# Apmāca modeli.
model.fit(X_train, y_train)

# Modeļa prognozes.
y_pred = model.predict(X_test)

# Aprēķina modeļa precizitāti.
model_accuracy = accuracy_score(y_test, y_pred)

# Aprēķina bāzes līniju (vienmēr min biežāko klasi).
most_common_class = y_train.mode()[0]
baseline_predictions = [most_common_class] * len(y_test)
baseline_accuracy = accuracy_score(y_test, baseline_predictions)

print(f"Modeļa precizitāte: {model_accuracy:.3f}")
print(f"Bāzes līnija:       {baseline_accuracy:.3f}")

if model_accuracy > baseline_accuracy:
    print("Modelis pārspēj bāzes līniju.")
elif model_accuracy < baseline_accuracy:
    print("Modelis nepārspēj bāzes līniju.")
else:
    print("Modelim un bāzes līnijai ir vienāda precizitāte.")
