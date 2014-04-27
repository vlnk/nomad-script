nomad-script
============

Qu'est ce que c'est?
--------------------
Un script pour interfacer le logiciel [NOMAD][1] développé par le GERAD.

[1]: http://www.gerad.ca/nomad/ "NOMAD"

Prérequis
---------

- Linux, BSD, Mac OSX
- Python 3.3+

Installation
------------

Il suffit d'entrer la commande suivante pour installer le script :
``pip3 install nomad-script``

L'installateur pip permet facilement de gérer l'installation et la désinstallation du script via la commande :
``pip3 uninstall nomad-script``

Pour plus d'informations, veuillez consulter la documentation de [pip][2].

[2]: http://www.pip-installer.org/en/latest/

Il est possible d'installer directement le script en téléchargeant celui-ci et en l'installant via la commande :
``
cd ../nomad-script
python3 setup.py install
``

Ou même de l'executer directement avec la commande :
``
python3 ../nomad-script/script/command.py
``

Configuration
-------------

Le script se lance avec la commande :
``
nomad-script <chemin de la boîte noire>
``

Un fichier de configuration est nécéssaire pour le bon fonctionnement du script. Il doit se trouver dans le même dossier que la boîte-noire.
``
bb_bin
	|---> bb.exe
	|---> config.txt
``

Voici un exemple du fichier **config.txt** :
``
# Ce fichier contient toute la configuration nécéssaire au bon fonctionnement du script. Veuillez ne modifier que ce qu'il y a après le '=', tous les paramètres seront intégrés au fonctionnement de NOMAD.
# Ce fichier doit être placé dans le même dossier que la boîte noire.

# Si la boîte noire accèpte des paramètres en ligne de commande. La valeur par défaut est NO. Si votre boîte noire accèpte des paramètres en lignes de commandes, veuillez mettre YES.
PARAMETERS_ON_COMMAND_LINE = no

# Le chemin du dossier d'instances, afin de les récupérer directement et de les traiter au fur et à mesure par NOMAD.
INSTANCES_DIRECTORY = ../instances_densite

# Algorithmic parameters
MAX_TIME =
MAX_BB_EVAL = 100
TMP_DIR = /tmp
DIRECTION_TYPE =
F_TARGET = 
INITIAL_MESH_SIZE =
LH_SEARCH =

# Output parameters
CACHE_FILE =
DISPLAY_ALL_EVAL =
DISPLAY_DEGREE =
DISPLAY_STATS = BBE OBJ : SOL 
HISTORY_FILE =
SOLUTION_FILE =
STATS_FILE =
``

Ce fichier contient tous les paramètres de NOMAD paramétrable par l'utilisateur pour une boîte noire. Les champs qui sont vides ne seront pas traités par le script.

Références
----------

+ C. Audet, S. Le Digabel, and C. Tribes. NOMAD user guide. Technical Report G-2009-37, Les cahiers du GERAD, 2009.

+ C. Audet and D. Orban. Finding optimal algorithmic parameters using derivative-free optimization. SIAM Journal on Optimization, 17(3):642–664, 2006.

+  C. Audet, G. Savard, and W. Zghal. Multiobjective optimization through a series of single- objective formulations. SIAM Journal on Optimization, 19(1):188–210, 2008.

+  C. Audet, G. Savard, and W. Zghal. A mesh adaptive direct search algorithm for multiob- jective optimization. European Journal of Operational Research, 204(3):545–556, 2010.

+  A.J. Booker, E.J. Cramer, P.D. Frank, J.M. Gablonsky, and J.E. Dennis, Jr. Movars: Multidisciplinary optimization via adaptive response surfaces. AIAA Paper 2007–1927, 2007.

+  A.J. Booker, J.E. Dennis, Jr., P.D. Frank, D.W. Moore, and D.B. Serafini. Managing surrogate objectives to optimize a helicopter rotor design – further experiments. AIAA Paper 1998–4717, Presented at the 8th AIAA/ISSMO Symposium on Multidisciplinary Analysis and Optimization, St. Louis, 1998.

+  A.J. Booker, J.E. Dennis, Jr., P.D. Frank, D.B. Serafini, and V. Torczon. Optimization using surrogate objectives on a helicopter test example. In J. Borggaard, J. Burns, E. Cliff, and S. Schreck, editors, Optimal Design and Control, Progress in Systems and Control Theory, pages 49–58, Cambridge, Massachusetts, 1998. Birkhäuser.

+  A.J. Booker, J.E. Dennis, Jr., P.D. Frank, D.B. Serafini, V. Torczon, and M.W. Trosset. A rigorous framework for optimization of expensive functions by surrogates. Structural and Multidisciplinary Optimization, 17(1):1–13, 1999.

+  A. Brooke, D. Kendrick, and A. Meeraus. GAMS: A Users’ Guide. The Scientific Press, Danvers, Massachusetts, 1988.

+  A.R. Conn and S. Le Digabel. Use of quadratic models with mesh-adaptive direct search for constrained black box optimization. Optimization Methods and Software, 28(1):139–158, 2013.

+  E.J. Cramer, J.E. Dennis, Jr., P.D. Frank, R.M. Lewis, and G.R. Shubin. Problem formu- lation for multidisciplinary optimization. In AIAA Symposium on Multidisciplinary Design Optimization, September 1993.

+ J.E. Dennis, Jr., C.J. Price, and I.D. Coope. Direct search methods for nonlinearly con- strained optimization using filters and frames. Optimization and Engineering, 5(2):123–144, 2004.

+ J.E. Dennis, Jr. and V. Torczon. Direct search methods on parallel machines. SIAM Journal on Optimization, 1(4):448–474, 1991.

+ K.R. Fowler, J.P. Reese, C.E. Kees, J.E. Dennis Jr., C.T. Kelley, C.T. Miller, C. Au- det, A.J. Booker, G. Couture, R.W. Darwin, M.W. Farthing, D.E. Finkel, J.M. Gablonsky, G. Gray, and T.G. Kolda. Comparison of derivative-free optimization methods for ground- water supply and hydraulic capture community problems. Advances in Water Resources, 31(5):743–757, 2008.

+ A.E. Gheribi, C. Audet, S. Le Digabel, E. Bélisle, C.W. Bale, and A.D. Pelton. Calculat- ing optimal conditions for alloy and process design using thermodynamic and properties databases, the FactSage software and the Mesh Adaptive Direct Search algorithm. CAL- PHAD: Computer Coupling of Phase Diagrams and Thermochemistry, 36:135–143, 2012.

+ A.E. Gheribi, C. Robelin, S. Le Digabel, C. Audet, and A.D. Pelton. Calculating all local minima on liquidus surfaces using the factsage software and databases and the mesh adap- tive direct search algorithm. The Journal of Chemical Thermodynamics, 43(9):1323–1330, 2011.

+ N.I.M. Gould, D. Orban, and Ph.L. Toint. CUTEr (and SifDec): A constrained and un- constrained testing environment, revisited. ACM Transactions on Mathematical Software, 29(4):373–394, 2003.

+ R.B. Gramacy. tgp: An R package for Bayesian nonstationary, semiparametric nonlinear regression and design by treed Gaussian process models. Journal of Statistical Software, 19(9):1–46, 2007.

+ R.B. Gramacy and S. Le Digabel. The mesh adaptive direct search algorithm with treed Gaussian process surrogates. Technical Report G-2011-37, Les cahiers du GERAD, 2011.

+ R.B. Gramacy and H.K.H. Lee. Bayesian treed Gaussian process models with an application to computer modeling. Journal of the American Statistical Association, 103(483):1119– 1130, 2008.

+ P. Hansen and N. Mladenović. Variable neighborhood search: principles and applications. European Journal of Operational Research, 130(3):449–467, 2001.

+ R.E. Hayes, F.H. Bertrand, C. Audet, and S.T. Kolaczkowski. Catalytic combustion kinetics: Using a direct search algorithm to evaluate kinetic parameters from light-off curves. The Canadian Journal of Chemical Engineering, 81(6):1192–1199, 2003.

+  D.R Jones, M. Schonlau, and W.J. Welch. Efficient global optimization of expensive black box functions. Journal of Global Optimization, 13(4):455–492, 1998.

+  L.A. Sweatlock K. Diest and D.E. Marthaler. Metamaterials design using gradient-free numerical optimization. Journal of Applied Physics, 108(8):1–5, 2010.

+  M. Kokkolaras, C. Audet, and J.E. Dennis, Jr. Mixed variable optimization of the number and composition of heat intercepts in a thermal insulation system. Optimization and Engineering, 2(1):5–29, 2001.

+  S. Le Digabel. Algorithm 909: NOMAD: Nonlinear optimization with the MADS algorithm. ACM Transactions on Mathematical Software, 37(4):44:1–44:15, 2011.