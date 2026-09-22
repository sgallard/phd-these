PERSPECTIVES

Generalizing the automated workflow

A broader research question raised by this thesis is: how can newspaper layout generation be extended from the automated construction of individual pages to the end-to-end generation of complete newspaper editions? The current work addresses several important components of this process, but still considers page generation largely as an isolated problem. Going beyond this setting requires jointly addressing the different decisions involved in producing a complete edition, from selecting and assigning content to pages, to determining their layouts and placing all relevant elements.

In particular, generating a full edition requires assigning each article to one of several pages according to its editorial section and the overall structure of the edition. This introduces an additional assignment problem on top of the template assignment and content-packing problems already jointly addressed by EvoPageGEN. Advertisement placement would further extend this formulation by introducing another class of placeable objects and additional constraints related to editorial and commercial requirements. The current implementation does not include advertisements because consistent metadata describing their historical coordinates and dimensions is not available in Melody’s layout records. This limitation therefore concerns the available data rather than the fundamental formulation of the optimization problem.

Addressing the complete workflow also raises a broader question of generalization: can the representations, objectives, and optimization mechanisms developed in this thesis transfer beyond the specific industrial context of Melody and the French regional press? Such a question would require evaluating whether the proposed approaches remain effective across different CMSs, publishers, markets, languages, or even structurally related layout domains such as magazines or user interfaces.

Ultimately, this perspective shifts the research problem from automating page construction to automating the production of a complete editorial layout, while investigating how such an approach can remain adaptable to different content, editorial structures, and production environments.

2 From large-print adaptation to personalized layouts (bridge gap btw large print and real production)

Large-print for real - gap not addressed

More generally:
RQ How can newspaper layouts dynamically adapt to individual readers’ visual and reading needs based on their preferences, interactions, and observed reading behavior?
The large-print study considered a common adaptation applied across readers. A natural next question is whether newspaper layouts could instead be adapted to individual visual and reading needs, potentially using interaction and behavioral feedback to refine the adaptation over time.

3 Towards human-guided layout optimization

The definition of editorial objectives and the evaluation of layouts both rely on human judgment, yet human feedback remains largely external to the optimization process. A key research question is therefore how expert and reader feedback could become part of the optimization loop itself.

4 From fixed pages to spatial and wearable media (VR/AR/smart glasses)

Now: Given a page, how do we arrange content on it?
Tomorrow: Demain : Given content, a reader, and a medium, how should the reading space itself be constructed?

The newspaper page has historically been shaped by the physical constraints of its medium. The transition from print to desktop displays, tablets, and smartphones has progressively relaxed some of these constraints while introducing new ones. Emerging spatial and wearable media may represent a further shift: rather than displaying a page on a fixed rectangular surface, they could allow newspaper content to be organized dynamically within the user's visual and physical space.
This raises a broader research question: how should editorial hierarchy, readability, navigation, and accessibility be rethought when the page is no longer a fixed two-dimensional object?