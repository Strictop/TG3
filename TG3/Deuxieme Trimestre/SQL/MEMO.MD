# Mémo  **SQL**


### Créer des tables :

```sql
CREATE TABLE table1 (id INTEGER PRIMARY KEY, nom TEXT, nom INTEGER);
```


### Insérer des données :

```sql
INSERT INTO table1 VALUES (73, "exemple", 33);
```

### Interroger les données :

#### Sélection :

- ```sql
    SELECT * FROM table1;
    ``` 
    Permet de tout sélectionner dans la table

- ```sql
    SELECT * FROM table1 nom > 20;
    ```
    Filtrer avec une seule condition

- ```sql
    SELECT * FROM table1 nom > 20 AND nom ="exemple";
    ```
    Filtrer avec plusieurs conditions

#### Trier les données :

- ```sql
    SELECT * FROM table1 WHERE nom > 21 ORDER BY age DESC;
    ``` 
    Permet de trier les données par orde croissant **`ASC`** et décroissant **`DESC`**

### Agréger les données :

- ```sql
    SELECT MAX(nom) FROM table1;*
    ```
    Fonction d'agrégation avec les instructions :
    1. `MAX()` pour récupérer la valeur maximum d’une colonne sur un ensemble de ligne.
    2. `MIN()` pour récupérer la valeur minimum d'une colonne sur un ensemble de ligne.
    3. `SUM()` pour calculer la somme sur un ensemble d’enregistrement
    4. `COUNT(*)` pour compte le nombre de lignes dans une table
    5. `COUNT(valeur)` pour compter le nombre de lignes qui contiennent la valeur

### Les jointures : 

- ```sql
    SELECT * FROM table1 INNER JOIN table2 O N table1.id_test = table2.id
    ```
    L'instructions **``INNER JOIN``** permet de créer une jointure entre la **table1** et la **table2**. Ensuite, les instructions **``ON table1.id_test = table2.id``** signifie qu'une ligne quelconque A de la **table1** devra être fusionnée avec la ligne B de la **table2** à condition que l'attribut **id_test** de la ligne A soit égal à l'attribut id de la ligne B.

### Modifications de données :

- ```sql
    UPDATE table1 SET nom_colonne = 'nouvelle valeur';
    ```
    Cette instruction permet de modifier des données déjà existante. Il bien entendu possible d'ajouter des conditions à celle-ci.

### Requêtes de suppression : 
    
- ```sql
    DELETE FROM table1 WHERE nom='exemple'
    ```

### Les domaines de valeurs : 

- ```sql
    CREATE TABLE table1 (nom VARCHAR(50), prenom CHAR(30));
    ```
    **`VARCHAR(n)`** / **`CHAR(n)`**: Chaîne de caractères de longueur variable (VARCHAR) ou fixe (CHAR) avec une longueur maximale spécifiée (n).

-  ```sql 
    CREATE TABLE table1 (age INT);
    ```
    **`INT`** / **`INTEGER`**: Nombre entier.

- ```sql 
    CREATE TABLE table1  (prix DECIMAL(10, 2));
    ```
    **`FLOAT`** / **`DOUBLE`** / **`DECIMAL`**: Nombres à virgule ou décimaux.

    **Précision :** 

 Le type **`FLOAT`** utilise 32 bits pour représenter les nombres à virgule flottante, offrant une précision d'environ 7 chiffres décimaux.
        
 Le type **`DOUBLE`** utilise 64 bits, offrant une précision plus élevée d'environ 15 chiffres décimaux.

- ```sql 
    CREATE TABLE table1 (est_actif BOOLEAN);
    ```
    **`BOOLEAN`** / **`BIT`**: Pour stocker des valeurs de vérité (VRAI ou FAUX).

- ```sql
    CREATE TABLE table1 (genre ENUM('Homme', 'Femme', 'Autre'));
    ```
    **`ENUM`**: Énumération, pour définir une liste de valeurs possibles.

### Les domaines de valeurs :
- ```sql 
    CREATE TABLE table1 (est_actif BOOLEAN);
    ```