import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

def prediction(TextExtracted): #upgrades: make the model already knowing of everything
    # csv data base transfer to an array
    df = pd.read_csv('/language-identification-datasets.csv')

    # division in 2 different arrays (1 for text & 1 for language)
    x = df['Text']
    y = df['Language']
    # z = df['ID']
    x_train = x[0:24326]
    y_train = y[0:24326]
    # y_test = y[24300:31014]
    # x_test = x[24300:31014]
    # z_test = z[24300:31014]

    # model creation
    model = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', DecisionTreeClassifier())
    ])

    # learning phase
    model.fit(x_train, y_train)

    # model evaluation
    y_pred = model.predict(TextExtracted)
    print(y_pred)
    # pd.DataFrame(y_pred, z_test).to_csv('ModèleFinale.csv')
