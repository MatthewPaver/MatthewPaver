############################################################################
### Written by Gaojie Jin and updated by Xiaowei Huang, 2021
###
### For a 2-nd year undergraduate student competition on 
### the robustness of deep neural networks, where a student 
### needs to develop 
### 1. an attack algorithm, and 
### 2. an adversarial training algorithm
###
### The score is based on both algorithms. 
############################################################################


import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
import torchvision
from torchvision import transforms
from torch.autograd import Variable
import argparse
import time
import copy

# input id
id_ = 201582813

# setup training parameters
parser = argparse.ArgumentParser(description='PyTorch MNIST Training')
parser.add_argument('--batch-size', type=int, default=128, metavar='N',
                    help='input batch size for training (default: 128)')
parser.add_argument('--test-batch-size', type=int, default=128, metavar='N',
                    help='input batch size for testing (default: 128)')
parser.add_argument('--epochs', type=int, default=10, metavar='N',
                    help='number of epochs to train')
parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate')
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='disables CUDA training')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')


args = parser.parse_args(args=[]) 

# judge cuda is available or not
use_cuda = not args.no_cuda and torch.cuda.is_available()
#device = torch.device("cuda" if use_cuda else "cpu")
device = torch.device("cpu")

torch.manual_seed(args.seed)
kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}

############################################################################
################    don't change the below code    #####################
############################################################################
train_set = torchvision.datasets.FashionMNIST(root='data', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True)

test_set = torchvision.datasets.FashionMNIST(root='data', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))
test_loader = DataLoader(test_set, batch_size=args.batch_size, shuffle=True)

# define fully connected network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.fc4(x)
        output = F.log_softmax(x, dim=1)
        return output

##############################################################################
#############    end of "don't change the below code"   ######################
##############################################################################



#Basic Iterative Method (BIM) attack
def bim_attack(model, X, y, device, epsilon, alpha, iterations):
    model.eval()
    torch.set_grad_enabled(True)
    X_adv = X.detach().clone()

    for i in range(iterations):
        X_adv.requires_grad = True

        output = model(X_adv)
        loss = F.nll_loss(output, y)

        model.zero_grad()
        loss.backward()
        data_grad = X_adv.grad.data

        X_adv = X_adv.detach() + alpha * data_grad.sign()
        eta = torch.clamp(X_adv - X, min=-epsilon, max=epsilon)
        X_adv = torch.clamp(X + eta, min=0, max=1).detach()

    return X_adv

#Projected Gradient Descent (PGD) attack
def pgd_attack(model, X, y, device, epsilon, alpha, iterations):
    # Start with the initial perturbed image
    model.eval()
    torch.set_grad_enabled(True)
    X_adv = X.detach().clone() + 0.001 * torch.randn(X.shape).to(device)

    for i in range(iterations):
        X_adv.requires_grad = True

        # Forward pass
        output = model(X_adv)
        loss = F.nll_loss(output, y)

        # Zero all existing gradients
        model.zero_grad()

        # Backward pass
        loss.backward()
        data_grad = X_adv.grad.data

        # PGD update
        X_adv = X_adv.detach() + alpha * data_grad.sign()
        eta = torch.clamp(X_adv - X, min=-epsilon, max=epsilon)
        X_adv = torch.clamp(X + eta, min=0, max=1).detach()

    return X_adv

#Fast Gradient Sign Method (FGSM) attack
def fgsm_attack(model, X, y, device, epsilon=0.1, alpha=0.01, iterations=10):
    # Ensure model is in evaluation mode
    model.eval()
    torch.set_grad_enabled(True)

    # Initialize perturbed image as the input image
    X_adv = X.detach().clone()

    for i in range(iterations):
        # Set requires_grad attribute of tensor. Important for Attack
        X_adv.requires_grad = True

        # Forward pass
        output = model(X_adv)
        loss = F.nll_loss(output, y)

        # Zero all existing gradients
        model.zero_grad()

        # Calculate gradients of model in backward pass
        loss.backward()

        # Collect datagrad
        data_grad = X_adv.grad.data

        # FGSM update on data
        sign_data_grad = data_grad.sign()
        X_adv = X_adv + alpha * sign_data_grad

        # Clip X_adv to maintain pixel values in the [-epsilon, epsilon] range
        X_adv = torch.clamp(X_adv, X - epsilon, X + epsilon).detach()

    return X_adv

#Iterative Fast Gradient Sign Method (IFGSM) attack
def ifgsm_attack(model, X, y, device, epsilon, alpha, iterations):
    X_adv = X.detach().clone()

    for i in range(iterations):
        X_adv.requires_grad = True

        output = model(X_adv)
        loss = F.nll_loss(output, y)

        model.zero_grad()
        loss.backward()
        data_grad = X_adv.grad.data

        X_adv = X_adv.detach() + alpha * data_grad.sign()
        eta = torch.clamp(X_adv - X, min=-epsilon, max=epsilon)
        X_adv = torch.clamp(X + eta, min=0, max=1).detach()

    return X_adv


from art.attacks.evasion import AutoAttack
from art.estimators.classification import PyTorchClassifier

def adv_attack(model, X, y, device, epsilon = 0.1):
    # Parameters for attacks
    epsilon = 0.1
    alpha = 0.01
    iterations = 10

    # Define PyTorch attack functions
    attack_functions = {
        'pgd': lambda: pgd_attack(model, X, y, device, epsilon, alpha, iterations),
        'bim': lambda: bim_attack(model, X, y, device, epsilon, alpha, iterations),
        'fgsm': lambda: fgsm_attack(model, X, y, device, epsilon),
        'ifgsm': lambda: ifgsm_attack(model, X, y, device, epsilon, alpha, iterations),
    }

    # Define ART attacks
    classifier = PyTorchClassifier(model=model, clip_values=(0, 1), loss=F.nll_loss, input_shape=X.shape[1:], nb_classes=10)
    art_attacks = {
        'autoattack': AutoAttack(classifier),
    }


    best_attack = None
    best_score = float('inf')
    best_adv_x = None

    # Run PyTorch attacks
    for attack_name, attack_func in attack_functions.items():
        try:
            adv_x = attack_func()
            score = evaluate_attack_effectiveness(model, adv_x, y, device)
            if score < best_score:
                best_score = score
                best_attack = attack_name
                best_adv_x = adv_x
        except Exception as e:
            print(f"Error in PyTorch attack {attack_name}: {e}")

    # Convert to numpy for ART attacks
    X_np = X.detach().cpu().numpy()
    y_np = y.detach().cpu().numpy()

    # Run ART attacks
    for attack_name, attack in art_attacks.items():
        try:
            adv_x_np = attack.generate(x=X_np)
            adv_x = torch.tensor(adv_x_np).to(device)
            score = evaluate_attack_effectiveness(model, adv_x, y, device)
            if score < best_score:
                best_score = score
                best_attack = attack_name
                best_adv_x = adv_x
        except Exception as e:
            print(f"Error in ART attack {attack_name}: {e}")

    return best_adv_x if best_adv_x is not None else X

# Evaluate the effectiveness of an attack
def evaluate_attack_effectiveness(model, X_adv, y, device):
    model.eval()
    X_adv_tensor = torch.tensor(X_adv).to(device)
    y = y.to(device)
    with torch.no_grad():
        output = model(X_adv_tensor)
        loss = F.nll_loss(output, y)
        _, predicted = output.max(1)
        accuracy = predicted.eq(y).sum().item() / y.size(0)
    return accuracy


# Train function
def train(args, model, device, train_loader, optimizer, epoch, max_epoch):
    model.train()
    epsilon = 0.1 + (epoch / max_epoch) * 0.1  # Dynamic Epsilon Adjustment

    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        data = data.view(data.size(0), -1)

        # Generate adversarial data for the current batch
        adv_data = adv_attack(model, data, target, device, epsilon=epsilon)

        # Combine original and adversarial data
        combined_data = torch.cat((data, adv_data), 0)
        combined_target = torch.cat((target, target), 0)

        # Compute loss and backpropagation
        optimizer.zero_grad()
        output = model(combined_data)
        loss = F.nll_loss(output, combined_target)  # Consider weighted loss
        loss.backward()
        optimizer.step()

#predict function
def eval_test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            data = data.view(data.size(0),28*28)
            output = model(data)
            test_loss += F.nll_loss(output, target, size_average=False).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)
    test_accuracy = correct / len(test_loader.dataset)
    return test_loss, test_accuracy

def eval_adv_test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            data = data.view(data.size(0),28*28)
            adv_data = adv_attack(model, data, target, device=device)
            output = model(adv_data)
            test_loss += F.nll_loss(output, target, size_average=False).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)
    test_accuracy = correct / len(test_loader.dataset)
    return test_loss, test_accuracy

#main function, train the dataset and print train loss, test loss for each epoch
def train_model():
    model = Net().to(device)
    
    optimizer = optim.Adam(model.parameters(), lr=args.lr)  # Using Adam optimizer
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.9)  # LR scheduler

    best_loss = float('inf')
    early_stopping_counter = 0

    max_epoch = args.epochs

    for epoch in range(1, args.epochs + 1):
        start_time = time.time()
        
        # Training
        train(args, model, device, train_loader, optimizer, epoch, max_epoch)
        scheduler.step()  # Update learning rate
        
        # Evaluation
        trn_loss, trn_acc = eval_test(model, device, train_loader)
        adv_loss, adv_acc = eval_adv_test(model, device, train_loader)


        # Early stopping check
        if adv_loss < best_loss:
            best_loss = adv_loss
            early_stopping_counter = 0
        else:
            early_stopping_counter += 1
            if early_stopping_counter > 2:  # Stop if no improvement in 3 epochs
                print("Early stopping triggered")
                break
        
        #print trnloss and testloss
        print('Epoch '+str(epoch)+': '+str(int(time.time()-start_time))+'s', end=', ')
        print('trn_loss: {:.4f}, trn_acc: {:.2f}%'.format(trn_loss, 100. * trn_acc), end=', ')
        print('adv_loss: {:.4f}, adv_acc: {:.2f}%'.format(adv_loss, 100. * adv_acc))

    # Final evaluations
    adv_tstloss, adv_tstacc = eval_adv_test(model, device, test_loader)
    print('Your estimated attack ability, by applying your attack method on your own trained model, is: {:.4f}'.format(1/adv_tstacc))
    print('Your estimated defence ability, by evaluating your own defence model over your attack, is: {:.4f}'.format(adv_tstacc))
    ################################################################################################
    ## end of training method
    ################################################################################################
    
    #save the model
    save_path = '/Users/mattpaver/Desktop/201582813/' + str(id_) + '.pt'
    torch.save(model.state_dict(), save_path)
    return model

#compute perturbation distance
def p_distance(model, train_loader, device):
    p = []
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        data = data.view(data.size(0),28*28)
        data_ = copy.deepcopy(data.data)
        adv_data = adv_attack(model, data, target, device=device)
        p.append(torch.norm(data_-adv_data, float('inf')))
    print('epsilon p: ',max(p))

    
################################################################################################
## Note: below is for testing/debugging purpose, please comment them out in the submission file
################################################################################################
    
#Comment out the following command when you do not want to re-train the model
#In that case, it will load a pre-trained model you saved in train_model()
model = train_model()

#Call adv_attack() method on a pre-trained model'
#the robustness of the model is evaluated against the infinite-norm distance measure
#important: MAKE SURE the infinite-norm distance (epsilon p) less than 0.11 !!!
p_distance(model, train_loader, device)