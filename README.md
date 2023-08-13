# HealthInfoRecognizer

https://www.csail.mit.edu/news/large-language-models-help-decipher-clinical-notes

http://clinicalml.org/publication/agrawal-2022-large/

https://hacknosis.hackerearth.com/#overview

Implementation of task 5 from paper Example:
Input:
Seroquel has not worked. Multiple antidepressants have not worked. The patient reports that he moved in with a gal after his divorce and she basically tells him that alcohol will take his problems away. The patient does try to attend NA and AA meetings, but reports that benzodiazepines are must. The patient experiences frequent panic attacks for a long time. He could not drive a car or even go to the grocery store.

Output:
```
{
        "dosage": "50mg",
        "frequency": "Once daily",
        "medication_name": "Seroquel",
        "reason": "Treatment of schizophrenia",
        "status": "discontinued"
      },
      {
        "dosage": "N/A",
        "frequency": "N/A",
        "medication_name": "Multiple antidepressants",
        "reason": "Depression treatment",
        "status": "discontinued"
      },
      {
        "dosage": "N/A",
        "frequency": "N/A",
        "medication_name": "Alcohol",
        "reason": "Not a medication",
        "status": "active"
      },
      {
        "dosage": "N/A",
        "frequency": "N/A",
        "medication_name": "Benzodiazepines",
        "reason": "Treatment of anxiety and panic disorders",
        "status": "active"
      }
    ]

```

    
