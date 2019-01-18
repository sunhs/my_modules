import os
import pickle

######################################################################
# Needed by my_modules.
######################################################################
# Names and paths.
PROJ_ROOT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', '..'
)
APP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
DATA_DIR = os.path.join(PROJ_ROOT_DIR, 'data')
MODEL_DIR = os.path.join(
    APP_DIR, 'save_dir',
    'config_{}'.format(os.path.basename(__file__).rsplit('.')[0].split('_')[1])
)
PRETRAIN_PATH = ''
STATE_DIR = os.path.join(MODEL_DIR, 'states')
STATE_PREFIX = 'model'
STATE_INDEX = None
SAVE_EPOCH_FREQ = 10

# Hypers and devices.
MAX_EPOCHS = 30
BATCH_SIZE = {'train': 32, 'test': 1}
PARAM_GROUPS = [
    {
        'params': ['default'],
        'lr': 1e-4,
        'weight_decay': 1e-5
    }, {
        'params': ['psp', 'fuse54', 'fuse43', 'fuse32', 'color_head'],
        'lr': 1e-3,
        'weight_decay': 1e-5
    }
]
GPUS = []
DEFAULT_GPU = 2
NUM_WORKERS = 8

if not os.path.exists(STATE_DIR):
    os.makedirs(STATE_DIR)

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

with open(os.path.join(MODEL_DIR, 'log.pkl'), 'wb') as f:
    log = {'train': {'loss': []}, 'test': {'loss': []}}
    pickle.dump(log, f)

with open(os.path.join(MODEL_DIR, 'train_log.pkl'), 'wb') as f:
    train_log = []
    pickle.dump(train_log, f)
