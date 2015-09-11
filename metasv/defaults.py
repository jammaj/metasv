MIN_SV_LENGTH = 50
MAX_SV_LENGTH = 1000000
OVERLAP_RATIO = 0.5
WIGGLE = 100
INS_WIGGLE = 100
SVS_SUPPORTED = set(["DEL", "DUP", "INS", "INV"])
SVS_ASSEMBLY_SUPPORTED = set(["DEL", "INS" , "INV"])

# For generating candidate intervals for insertion assembly
MIN_SUPPORT = 5
MIN_SUPPORT_FRAC = 0
MAX_INTERVALS = 10000
SC_PAD = 500
SC_MIN_SOFT_CLIP = 20
SC_MIN_AVG_BASE_QUAL = 20
SC_MIN_MAPQ = 5
SC_MAX_NM = 10
SC_MIN_MATCHES = 50

ISIZE_MIN = 250
ISIZE_MAX = 450
ISIZE_MEAN = 350.0
ISIZE_SD = 50.0

# For assembly read-extraction
EXTRACTION_MAX_READ_PAIRS = 10000
EXTRACTION_MAX_NM = 5
EXTRACTION_MAX_INTERVAL_TRUNCATION = 10000
EXTRACTION_TRUNCATION_PAD = 4000

# For running SPAdes
ASSEMBLY_MAX_TOOLS = 1
SPADES_TIMEOUT = 300  # in seconds
SPADES_PAD = 500
SPADES_MAX_INTERVAL_SIZE = 50000

# For running AGE
AGE_TIMEOUT = 300  # in seconds
AGE_MIN_CONTIG_LENGTH = 200
AGE_PAD = 500
AGE_MAX_REGION_LENGTH = 1000000
AGE_MAX_INTERVAL_TRUNCATION = 10000
AGE_TRUNCATION_PAD = 2000
AGE_DIST_TO_BP = 400

# For genotyping
GT_WINDOW = 100
GT_NORMAL_FRAC = 0.05
