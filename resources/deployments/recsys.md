# Deployment details for TRS

- TRS was deployed successfully in a preprod server of melody, currently serving as a pilot functionality to publihebdos (actu.fr) press group
- via a Python API REST.
- Two important notes about  extra implemented features that Melody required after finishing the implementation and analysis of TRS
1.  In particular, the necessity to relax the image constraint to allow to use the full text capacity matrix (i.e., declare as addmissible templates with more images slots that the required, if the body text is in the corresponding interval of the capacity matrix (note: explain this better based on the definition of text caapacity matrix)). At the beginning and during the development and analysis of TRS in this thesis, this was not the case, as explained in this chapter (i.e., they asked to use the exact number of image slots for the required web article)
2. Curiosly, thpulbihebdos group did not like that the newly implemented GUI for this TRS highlight the recommendation in a special block (marked as "intelligent recommendation"). That is why we designed a variant of TRS, by increasing N of Top-N to half of the total set of addmisible templates, and CW_th adjusted by adapting it: the idea was that CW_th is the minimum (to ensure diversity) that allow to have N/2 recommended templates (i.e. if lower, it will require to output <N/2).
Thanks to this adaptation, the GUI just lists templates BUT in the order outputed by the TRS mechanism. This way, it does not have the impression that is a intelligent ai-based recommmendation, but just a re-ranking, which pleased publihebdos press group.

