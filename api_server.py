#!/usr/bin/env python3
"""
API Server for Payroll Data Structures Demo
Provides REST endpoints for stack and queue operations
"""

from flask import Flask, jsonify
from ds.stack import Stack
from ds.queue import Queue, PriorityQueue
import json

app = Flask(__name__)

# Global data structures for demo
payroll_stack = Stack()
payroll_queue = Queue()

@app.route('/api/stack/push/<item>')
def stack_push(item):
    """Push an item onto the stack"""
    try:
        payroll_stack.push(item)
        return jsonify({
            'status': 'success', 
            'item': item, 
            'size': payroll_stack.size()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/stack/pop')
def stack_pop():
    """Pop an item from the stack"""
    try:
        if not payroll_stack.is_empty():
            item = payroll_stack.pop()
            return jsonify({
                'status': 'success', 
                'item': item, 
                'size': payroll_stack.size()
            })
        return jsonify({'status': 'error', 'message': 'Stack is empty'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/stack/peek')
def stack_peek():
    """Peek at the top item of the stack"""
    try:
        if not payroll_stack.is_empty():
            item = payroll_stack.peek()
            return jsonify({'status': 'success', 'item': item})
        return jsonify({'status': 'error', 'message': 'Stack is empty'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/stack/size')
def stack_size():
    """Get the size of the stack"""
    try:
        return jsonify({
            'status': 'success',
            'size': payroll_stack.size(),
            'is_empty': payroll_stack.is_empty()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/queue/enqueue/<item>')
def queue_enqueue(item):
    """Enqueue an item to the queue"""
    try:
        payroll_queue.enqueue(item)
        return jsonify({
            'status': 'success', 
            'item': item, 
            'size': payroll_queue.size()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/queue/dequeue')
def queue_dequeue():
    """Dequeue an item from the queue"""
    try:
        if not payroll_queue.is_empty():
            item = payroll_queue.dequeue()
            return jsonify({
                'status': 'success', 
                'item': item, 
                'size': payroll_queue.size()
            })
        return jsonify({'status': 'error', 'message': 'Queue is empty'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/queue/front')
def queue_front():
    """Get the front item of the queue"""
    try:
        if not payroll_queue.is_empty():
            item = payroll_queue.front()
            return jsonify({'status': 'success', 'item': item})
        return jsonify({'status': 'error', 'message': 'Queue is empty'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/queue/size')
def queue_size():
    """Get the size of the queue"""
    try:
        return jsonify({
            'status': 'success',
            'size': payroll_queue.size(),
            'is_empty': payroll_queue.is_empty()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/stack/all')
def stack_all():
    """Get all items in the stack"""
    try:
        items = payroll_stack.get_all() if hasattr(payroll_stack, 'get_all') else []
        return jsonify({
            'status': 'success',
            'items': items,
            'size': payroll_stack.size()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/queue/all')
def queue_all():
    """Get all items in the queue"""
    try:
        items = payroll_queue.get_all() if hasattr(payroll_queue, 'get_all') else []
        return jsonify({
            'status': 'success',
            'items': items,
            'size': payroll_queue.size()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'payroll-data-structures-api'})

@app.route('/api/')
def api_info():
    """API information endpoint"""
    return jsonify({
        'service': 'Payroll Data Structures API',
        'version': '1.0.0',
        'endpoints': {
            'stack': {
                'push': '/api/stack/push/<item>',
                'pop': '/api/stack/pop',
                'peek': '/api/stack/peek',
                'size': '/api/stack/size',
                'all': '/api/stack/all'
            },
            'queue': {
                'enqueue': '/api/queue/enqueue/<item>',
                'dequeue': '/api/queue/dequeue',
                'front': '/api/queue/front',
                'size': '/api/queue/size',
                'all': '/api/queue/all'
            },
            'info': {
                'health': '/api/health',
                'info': '/api/'
            }
        }
    })

if __name__ == '__main__':
    print("🚀 Starting Payroll Data Structures API Server...")
    print("📊 Available endpoints:")
    print("  Stack:  /api/stack/*")
    print("  Queue:  /api/queue/*")
    print("  Health: /api/health")
    print("  Info:   /api/")
    print("")
    print("🌐 Server running on http://0.0.0.0:5000")
    
    app.run(host='0.0.0.0', port=5000, debug=True)