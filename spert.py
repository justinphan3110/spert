import argparse

from args import train_argparser, eval_argparser
from config_reader import process_configs
from spert import input_reader
from spert.spPhoBert_trainer import SpPhoBERTTrainer
from spert.spert_trainer import SpERTTrainer
from spert.trainer import BaseTrainer


def __train(run_args):
    trainer = SpERTTrainer(run_args)
    trainer.train(train_path=run_args.train_path, valid_path=run_args.valid_path,
                  types_path=run_args.types_path, input_reader_cls=input_reader.JsonInputReader)

def __train_vn(run_args):
    trainer = SpPhoBERTTrainer(run_args)
    trainer.train(train_path=run_args.train_path, valid_path=run_args.valid_path,
                  types_path=run_args.types_path, input_reader_cls=input_reader.JsonInputReader)



def __eval_vn(run_args):
    trainer = SpPhoBERTTrainer(run_args)
    trainer.eval(dataset_path=run_args.dataset_path, types_path=run_args.types_path, input_reader_cls=input_reader.JsonInputReader)


def __eval(run_args):
    trainer = SpPhoBERTTrainer(run_args)
    trainer.eval(dataset_path=run_args.dataset_path, types_path=run_args.types_path,
                 input_reader_cls=input_reader.JsonInputReader)

def __predict(run_args):
    trainer = SpPhoBERTTrainer(run_args)
    trainer.predict(dataset_path=run_args.dataset_path, types_path=run_args.types_path,
                 input_reader_cls=input_reader.BatchJsonInputReader)



def _train():
    arg_parser = train_argparser()
    process_configs(target=__train, arg_parser=arg_parser)


def _train_vn():
    arg_parser = train_argparser()
    process_configs(target=__train_vn, arg_parser=arg_parser)


def _eval_vn():
    arg_parser = eval_argparser()
    process_configs(target=__eval_vn, arg_parser=arg_parser)


def _eval():
    arg_parser = eval_argparser()
    process_configs(target=__eval, arg_parser=arg_parser)

def _predict():
    arg_parser = eval_argparser()
    process_configs(target=__predict, arg_parser=arg_parser)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('mode', type=str, help="Mode: 'train' or 'eval'")
    args, _ = arg_parser.parse_known_args()

    if args.mode == 'train':
        _train()
    elif args.mode == "train_vn":
        _train_vn()
    elif args.mode == 'eval':
        _eval()
    elif args.mode == 'predict':
        _predict()
    else:
        raise Exception("Mode not in ['train', 'eval'], e.g. 'python spert.py train ...'")
