# Dataset

To instantiate the definitions, two datasets were provided by melody.

## Publihebdos archive

The company Actu.fr provided access to their premium dataset of their issue entitled Publihebdos

### Set of templates

Specifically, they provide a set of XX (note: check in recsys section) templates, each one defined in an XML the following
- id
- width and height
- number of image slots
- number of characters of body text it can allocate (when all image slots are occupied)
- zoning of each block, for each one
    - class
    - bbox relative to the dimensions of the template

Note that the bboxes can overlap between them. In fact, in practice what happens is that the body text is one big block in the background and the rest of the blocks are on top of it

Also, a JPG image of the template is provided, with placeholders to visualize it.

(insert image)

### Usage log

Additionally, they provide a CSV with usage logs during the last 6 months of each template in the dataset, in the form

id;overall usage; month1; month2....

This usage shows a huge long tail, which justifies the necessity of having a mechanism to avoid long tails

< insert plot>

### Statistics

TODO


## La Provence archive

The company La provence provided access to their premium dataset of both templates and historical page layouts

### Set of templates

THey provide a set of 345 templates, analog to publihebdos (same information in both XML and JPG)

#### Statistics

TODO

### Set of pages

They also provide a set of ZZ historical page layouts done in melody by operators.

Each page corresponds to a front or internal page of the regional daily La Provence, in a XML format with the following information

- ID
- width and height
- margins
- for each article
    - id
    - x, y, width and height relative to the absolute page (i.e. ignoring the page margins)
    - presence of title 
    - presence of subtitle
    - nuber of images allocated
    - number of characters of body text allocated
    - template id
    - Template <id> XML. That means, a deep copy of the template id XML file.

Advertisements are not always present in the XML since usually they are hardcoded in the page.
Articles does not always respet template width and height (note: do a matching with the notion of elasticity in chapter 5)
also, articles can use a different number of the images that the template has available, but always less or equal.

Additionally, a PDF version of the page was provided

(insert image)


#### Statistics 
TODO



## Preprocessing

To complete the information required for the developed methods in this thesis, it is necessary to do a preprocessing step on both the template and page datasets, for both clients

### Template preprocessing

First, since the bboxes does not represent the real topology of the internal blocs to compute layout similarity (\secref{section of gmn and tdiou}), each template was cleaned to discover the polygon that actually bound each bloc.
This was done using intersection and union operations of polygons to find the real polygon that described the body text block, surrounding the other blocks. This was done using CGAL library.

Then, the capacity matrix was calculated for each template in the way described in the definition of the capacity matrix.

The result was saved in a json file. Also, a new png representation was created to highlight the real topology of the template

(insert image)

### Page preprocessing


First, all front pages were discarded, since they follow different layout building principles. This was a requirement of melody

Then, all pages that include:
- overlapping or overflowing (i.e. outside of the boundaries of the page) articles, which describe an exporting error
- articles with templates that does not exists in the corresponding template dataset (la provence), which shows a desync error between versions of the datasets

were also discarded


Then, the remaining XXXX pages were classified:
- Pages where all articles have a width and height corresponding exactly to the selected template width and height (note: make a correspondance with elascitiy=0 in chapter 5). Number: cc
- pages where the previous is not the case, but with an absolute difference of less than 15%. Number: bb
- pages with a difference of above 15%. Number: aa
- pages with a single full page article. Number: dd


All admissible pages were used to train models, but only the first two were used as instances for the NSGA algorithm since they are more realistic with what that formulation attemps to model, as requested by melody. In the former case, this was not possible since there were not enough pages to do the training using only the first two.


