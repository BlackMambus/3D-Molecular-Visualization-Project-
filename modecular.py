import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem

mol = Chem.MolFromSmiles('CCO')  # Ethanol
AllChem.EmbedMolecule(mol)
mb = Chem.MolToMolBlock(mol)

view = py3Dmol.view(width=400, height=400)
view.addModel(mb, 'mol')
view.setStyle({'stick': {}})
view.zoomTo()
view.show()

